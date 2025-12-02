
export const TAX_BRACKETS = [
  { min: 0, max: 150000, rate: 0 },
  { min: 150001, max: 300000, rate: 0.05 },
  { min: 300001, max: 500000, rate: 0.10 },
  { min: 500001, max: 750000, rate: 0.15 },
  { min: 750001, max: 1000000, rate: 0.20 },
  { min: 1000001, max: 2000000, rate: 0.25 },
  { min: 2000001, max: 5000000, rate: 0.30 },
  { min: 5000001, max: Infinity, rate: 0.35 },
];

export const MAX_EXPENSE_DEDUCTION = 100000;
export const EXPENSE_RATE = 0.5;
export const PERSONAL_DEDUCTION = 60000;

export const calculateExpenses = (income) => {
  return Math.min(income * EXPENSE_RATE, MAX_EXPENSE_DEDUCTION);
};

export const calculateTax = (netTaxableIncome) => {
  let remainingIncome = netTaxableIncome;
  let totalTax = 0;

  for (const bracket of TAX_BRACKETS) {
    if (remainingIncome <= 0) break;

    const bracketRange = bracket.max - bracket.min + 1;
    // For the first bracket (0-150,000), the range is 150,001 effectively if we count 0? 
    // Actually the table says 1-150,000. 
    // Let's simplify: taxable amount in this bracket.
    
    // Logic:
    // If income is above bracket.min:
    // Taxable amount in this bracket = min(income, bracket.max) - bracket.min + 1 ?
    // No, simpler way:
    
    const taxableInBracket = Math.max(0, Math.min(netTaxableIncome, bracket.max) - Math.max(0, bracket.min - 1));
    // Wait, bracket.min is 150001. 
    // If income is 300,000.
    // Bracket 1 (0-150k): min(300k, 150k) - 0 = 150k. Tax = 0.
    // Bracket 2 (150k-300k): min(300k, 300k) - 150k = 150k. Tax = 150k * 0.05 = 7500.
    
    // Correct logic:
    const prevMax = bracket.min - 1;
    const taxableAmount = Math.max(0, Math.min(netTaxableIncome, bracket.max) - prevMax);
    
    totalTax += taxableAmount * bracket.rate;
  }

  return totalTax;
};

export const analyzeTax = (income, deductions = 0) => {
  const expenses = calculateExpenses(income);
  const netIncome = income - expenses - PERSONAL_DEDUCTION - deductions;
  const netTaxableIncome = Math.max(0, netIncome);
  
  const tax = calculateTax(netTaxableIncome);
  
  // Find current bracket
  const currentBracket = TAX_BRACKETS.find(b => netTaxableIncome >= b.min && netTaxableIncome <= b.max);
  
  // Find next lower bracket (to pay less tax rate on marginal income)
  // Actually, "bucket ก่อนหน้า" usually means dropping to a lower max rate.
  // E.g. if I am in 10% bracket (300k-500k), I want to drop to 5% bracket (150k-300k).
  // So target income is 300,000.
  
  let nextBracketTarget = null;
  let amountToDropBracket = 0;
  
  if (currentBracket && currentBracket.rate > 0) {
     // Find the bracket before this one
     const currentIndex = TAX_BRACKETS.indexOf(currentBracket);
     if (currentIndex > 0) {
         const prevBracket = TAX_BRACKETS[currentIndex - 1];
         // Target is the max of previous bracket
         const targetIncome = prevBracket.max;
         amountToDropBracket = netTaxableIncome - targetIncome;
         nextBracketTarget = {
             rate: prevBracket.rate,
             targetNetIncome: targetIncome,
             amountNeeded: amountToDropBracket
         };
     }
  }

  return {
    income,
    expenses,
    personalDeduction: PERSONAL_DEDUCTION,
    otherDeductions: deductions,
    netTaxableIncome,
    tax,
    currentBracket,
    nextBracketTarget
  };
};
