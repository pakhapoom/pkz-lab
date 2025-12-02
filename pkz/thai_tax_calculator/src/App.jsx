import React, { useState, useMemo } from 'react';
import IncomeInput from './components/IncomeInput';
import DeductionGroup from './components/DeductionGroup';
import ResultCard from './components/ResultCard';
import { DEDUCTION_GROUPS } from './data/deductions';
import { analyzeTax } from './utils/taxCalculator';

function App() {
  const [income, setIncome] = useState(0);
  const [deductions, setDeductions] = useState({});

  const handleDeductionChange = (id, value) => {
    setDeductions(prev => ({
      ...prev,
      [id]: value
    }));
  };

  const calculateTotalDeductions = () => {
    let total = 0;

    // Simple summation for now. 
    // In a real app, we would implement complex validation logic here 
    // (e.g. capping insurance at 100k, checking % limits).
    // For this version, we assume user enters valid amounts or we sum them up 
    // and let the user know if they exceed limits via hints, 
    // but strictly speaking the 'analyzeTax' function expects a single deduction number.
    // So we should sum them up here.

    // Note: Some items like double donation need special handling.
    // Let's handle the double donation logic here simply:

    Object.entries(deductions).forEach(([key, value]) => {
      if (key === 'donation_education') {
        total += value * 2;
      } else {
        total += value;
      }
    });

    return total;
  };

  const totalDeductions = calculateTotalDeductions();
  const analysisResult = useMemo(() => analyzeTax(income, totalDeductions), [income, totalDeductions]);

  return (
    <div className="app-container">
      <h1>🇹🇭 Thai Tax Calculator 2568</h1>

      <div className="grid-cols-2">
        <div className="input-section">
          <IncomeInput income={income} onChange={setIncome} />

          {DEDUCTION_GROUPS.map(group => (
            <DeductionGroup
              key={group.id}
              title={group.title}
              fields={group.fields}
              values={deductions}
              onChange={handleDeductionChange}
            />
          ))}
        </div>

        <div className="result-section">
          <div style={{ position: 'sticky', top: '2rem' }}>
            <ResultCard result={analysisResult} />

            <div style={{ marginTop: '1rem', textAlign: 'center', fontSize: '0.8rem', color: '#94a3b8' }}>
              <p>หมายเหตุ: การคำนวณนี้เป็นการประมาณการเบื้องต้น</p>
              <p>โปรดตรวจสอบความถูกต้องกับกรมสรรพากรอีกครั้ง</p>
            </div>
          </div>
        </div>
      </div>
    </div>
  );
}

export default App;
