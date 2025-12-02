import React, { useState } from 'react';

const DeductionGroup = ({ title, fields, values, onChange }) => {
    const [isOpen, setIsOpen] = useState(false);

    // Calculate total for this group
    const groupTotal = fields.reduce((sum, field) => sum + (values[field.id] || 0), 0);

    return (
        <div className="card" style={{ padding: '1rem 1.5rem' }}>
            <div
                style={{ display: 'flex', justifyContent: 'space-between', alignItems: 'center', cursor: 'pointer' }}
                onClick={() => setIsOpen(!isOpen)}
            >
                <div style={{ display: 'flex', alignItems: 'center', gap: '0.5rem' }}>
                    <h3>{title}</h3>
                    {groupTotal > 0 && (
                        <span className="badge badge-success">
                            ลดหย่อน {groupTotal.toLocaleString()} บาท
                        </span>
                    )}
                </div>
                <button className="btn" style={{ padding: '0.5rem', background: 'transparent' }}>
                    {isOpen ? '▲' : '▼'}
                </button>
            </div>

            {isOpen && (
                <div style={{ marginTop: '1.5rem' }}>
                    {fields.map((field) => (
                        <div key={field.id} className="input-group">
                            <label className="input-label" htmlFor={field.id}>
                                {field.label}
                            </label>
                            <input
                                id={field.id}
                                type="number"
                                className="input-field"
                                value={values[field.id] || ''}
                                onChange={(e) => onChange(field.id, Number(e.target.value))}
                                placeholder={field.placeholder || '0'}
                                min="0"
                            />
                            {field.hint && (
                                <p style={{ marginTop: '0.25rem', fontSize: '0.8rem', color: 'var(--text-secondary)' }}>
                                    {field.hint}
                                </p>
                            )}
                        </div>
                    ))}
                </div>
            )}
        </div>
    );
};

export default DeductionGroup;
