
import { analyzeTax } from './src/utils/taxCalculator.js';

const runTest = (income, deductions, expectedTax) => {
    const result = analyzeTax(income, deductions);
    console.log(`Income: ${income}, Deductions: ${deductions}`);
    console.log(`Net Taxable: ${result.netTaxableIncome}`);
    console.log(`Calculated Tax: ${result.tax}`);
    console.log(`Expected Tax: ${expectedTax}`);
    console.log(`Match: ${Math.abs(result.tax - expectedTax) < 0.01 ? 'PASS' : 'FAIL'}`);
    if (result.nextBracketTarget) {
        console.log(`Next Bracket Target: Net Income ${result.nextBracketTarget.targetNetIncome} (Rate ${result.nextBracketTarget.rate * 100}%)`);
        console.log(`Need to reduce income by: ${result.nextBracketTarget.amountNeeded}`);
    }
    console.log('-----------------------------------');
};

console.log('Running Tax Logic Tests...\n');

// Case 1: 300k income
// Exp: 100k (max 50% of 300k is 150k, capped at 100k) -> Wait, 50% of 300k is 150k. Max is 100k. So 100k.
// Personal: 60k
// Net: 300 - 100 - 60 = 140k.
// Tax: 0 (0-150k is exempt)
runTest(300000, 0, 0);

// Case 2: 500k income
// Exp: 100k
// Personal: 60k
// Net: 500 - 100 - 60 = 340k
// Tax:
// 0-150k: 0
// 150-300k: 150k * 5% = 7,500
// 300-340k: 40k * 10% = 4,000
// Total: 11,500
runTest(500000, 0, 11500);

// Case 3: 1M income
// Exp: 100k
// Personal: 60k
// Net: 1M - 100k - 60k = 840k
// Tax:
// 0-150k: 0
// 150-300k: 7,500
// 300-500k: 20,000
// 500-750k: 37,500
// 750-840k: 90k * 20% = 18,000
// Total: 83,000
runTest(1000000, 0, 83000);
