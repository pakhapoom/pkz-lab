import React from 'react';

const IncomeInput = ({ income, onChange }) => {
    return (
        <div className="card">
            <h2>รายได้ต่อปี</h2>
            <div className="input-group">
                <label className="input-label" htmlFor="income">
                    เงินได้พึงประเมิน (บาท)
                </label>
                <input
                    id="income"
                    type="number"
                    className="input-field"
                    value={income}
                    onChange={(e) => onChange(Number(e.target.value))}
                    placeholder="ระบุเงินได้ต่อปีของคุณ"
                    min="0"
                />
                <p style={{ marginTop: '0.5rem', fontSize: '0.875rem', color: 'var(--text-secondary)' }}>
                    *คำนวณแบบหักค่าใช้จ่าย 50% (สูงสุด 100,000 บาท) โดยอัตโนมัติ
                </p>
            </div>
        </div>
    );
};

export default IncomeInput;
