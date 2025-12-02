import React from 'react';

const ResultCard = ({ result }) => {
    const {
        income,
        expenses,
        personalDeduction,
        otherDeductions,
        netTaxableIncome,
        tax,
        currentBracket,
        nextBracketTarget
    } = result;

    const effectiveTaxRate = income > 0 ? (tax / income) * 100 : 0;

    return (
        <div className="card" style={{ border: '2px solid var(--primary-color)' }}>
            <h2 style={{ textAlign: 'center', marginBottom: '1.5rem' }}>สรุปภาษีที่ต้องชำระ</h2>

            <div style={{ textAlign: 'center', marginBottom: '2rem' }}>
                <div style={{ fontSize: '3rem', fontWeight: '800', color: 'var(--primary-color)' }}>
                    {tax.toLocaleString()} <span style={{ fontSize: '1.5rem' }}>บาท</span>
                </div>
                <p style={{ color: 'var(--text-secondary)' }}>
                    อัตราภาษีเฉลี่ย {effectiveTaxRate.toFixed(2)}%
                </p>
            </div>

            <div style={{ marginBottom: '1.5rem' }}>
                <div className="summary-item">
                    <span className="summary-label">เงินได้ทั้งปี</span>
                    <span className="summary-value">{income.toLocaleString()}</span>
                </div>
                <div className="summary-item">
                    <span className="summary-label">หักค่าใช้จ่าย (50% ไม่เกิน 100k)</span>
                    <span className="summary-value text-danger">-{expenses.toLocaleString()}</span>
                </div>
                <div className="summary-item">
                    <span className="summary-label">ค่าลดหย่อนส่วนตัว</span>
                    <span className="summary-value text-danger">-{personalDeduction.toLocaleString()}</span>
                </div>
                <div className="summary-item">
                    <span className="summary-label">ค่าลดหย่อนอื่นๆ</span>
                    <span className="summary-value text-danger">-{otherDeductions.toLocaleString()}</span>
                </div>
                <div className="summary-item" style={{ borderTop: '2px solid var(--border-color)', marginTop: '0.5rem', paddingTop: '0.5rem' }}>
                    <span className="summary-label" style={{ fontWeight: '600', color: 'var(--text-main)' }}>เงินได้สุทธิ</span>
                    <span className="summary-value" style={{ fontSize: '1.2rem' }}>{netTaxableIncome.toLocaleString()}</span>
                </div>
            </div>

            <div style={{ background: 'var(--bg-color)', padding: '1rem', borderRadius: '8px', marginBottom: '1rem' }}>
                <h4 style={{ marginBottom: '0.5rem' }}>ฐานภาษีสูงสุดของคุณ: {currentBracket ? `${(currentBracket.rate * 100)}%` : 'ยกเว้น'}</h4>
                <p style={{ fontSize: '0.9rem', color: 'var(--text-secondary)' }}>
                    {currentBracket
                        ? `เงินได้สุทธิในช่วง ${currentBracket.min.toLocaleString()} - ${currentBracket.max === Infinity ? 'ขึ้นไป' : currentBracket.max.toLocaleString()}`
                        : 'เงินได้สุทธิไม่เกิน 150,000 บาท ได้รับการยกเว้นภาษี'}
                </p>
            </div>

            {nextBracketTarget && (
                <div style={{ background: '#fef3c7', padding: '1rem', borderRadius: '8px', border: '1px solid #fcd34d' }}>
                    <h4 style={{ color: '#92400e', marginBottom: '0.5rem' }}>💡 คำแนะนำลดหย่อนภาษี</h4>
                    <p style={{ color: '#92400e', fontSize: '0.95rem' }}>
                        หากคุณหาค่าลดหย่อนเพิ่มอีก <strong>{nextBracketTarget.amountNeeded.toLocaleString()} บาท</strong>
                        เงินได้สุทธิจะลดลงเหลือ {nextBracketTarget.targetNetIncome.toLocaleString()} บาท
                        ซึ่งจะทำให้ส่วนที่เกินเสียภาษีในอัตราลดลงเหลือ <strong>{(nextBracketTarget.rate * 100)}%</strong>
                    </p>
                    <p style={{ marginTop: '0.5rem', fontWeight: '600', color: '#92400e' }}>
                        ประหยัดภาษีได้เพิ่ม: {(nextBracketTarget.amountNeeded * currentBracket.rate).toLocaleString()} บาท
                    </p>
                </div>
            )}
        </div>
    );
};

export default ResultCard;
