export const DEDUCTION_GROUPS = [
    {
        id: 'family',
        title: 'กลุ่มส่วนตัวและครอบครัว',
        fields: [
            { id: 'spouse', label: 'คู่สมรส (ไม่มีเงินได้)', placeholder: '60,000', hint: 'ลดหย่อนได้ 60,000 บาท' },
            { id: 'child', label: 'บุตร (คนละ 30,000 บาท)', placeholder: 'ระบุจำนวนเงินรวม', hint: 'บุตรคนที่ 2 เกิดตั้งแต่ปี 2561 ได้คนละ 60,000 บาท' },
            { id: 'parents', label: 'ค่าอุปการะบิดามารดา', placeholder: 'ระบุจำนวนเงินรวม', hint: 'คนละ 30,000 บาท (อายุ 60 ปีขึ้นไป)' },
            { id: 'disabled', label: 'ค่าอุปการะผู้พิการ', placeholder: 'ระบุจำนวนเงินรวม', hint: 'คนละ 60,000 บาท' },
            { id: 'child_birth', label: 'ค่าฝากครรภ์และคลอดบุตร', placeholder: 'จ่ายจริงไม่เกิน 60,000', hint: 'ตามที่จ่ายจริง สูงสุดไม่เกิน 60,000 บาท' },
        ]
    },
    {
        id: 'insurance',
        title: 'กลุ่มประกันและเงินออม',
        fields: [
            { id: 'social_security', label: 'เงินสมทบประกันสังคม', placeholder: 'สูงสุด 9,000', hint: 'ตามที่จ่ายจริง สูงสุดไม่เกิน 9,000 บาท' },
            { id: 'life_insurance', label: 'เบี้ยประกันชีวิต', placeholder: 'สูงสุด 100,000', hint: 'รวมกับประกันสุขภาพตนเองไม่เกิน 100,000 บาท' },
            { id: 'health_insurance', label: 'เบี้ยประกันสุขภาพตนเอง', placeholder: 'สูงสุด 25,000', hint: 'สูงสุด 25,000 บาท (แต่วงเงินรวมประกันชีวิตไม่เกิน 100,000)' },
            { id: 'parents_health_insurance', label: 'เบี้ยประกันสุขภาพบิดามารดา', placeholder: 'สูงสุด 15,000', hint: 'สูงสุด 15,000 บาท' },
            { id: 'pension_insurance', label: 'เบี้ยประกันชีวิตแบบบำนาญ', placeholder: '15% ไม่เกิน 200,000', hint: 'ลดหย่อนได้ 15% ของเงินได้ สูงสุด 200,000 บาท' },
            { id: 'rmf', label: 'กองทุน RMF', placeholder: '30% ไม่เกิน 500,000', hint: 'ลดหย่อนได้ 30% ของเงินได้ สูงสุด 500,000 บาท' },
            { id: 'ssf', label: 'กองทุน SSF', placeholder: '30% ไม่เกิน 200,000', hint: 'ลดหย่อนได้ 30% ของเงินได้ สูงสุด 200,000 บาท' },
            { id: 'thaiesg', label: 'กองทุน Thai ESG', placeholder: '30% ไม่เกิน 300,000', hint: 'ลดหย่อนได้ 30% ของเงินได้ สูงสุด 300,000 บาท' },
            { id: 'pvd', label: 'กองทุนสำรองเลี้ยงชีพ / กบข.', placeholder: '15% ไม่เกิน 500,000', hint: 'ส่วนที่สะสมเพิ่ม' },
        ]
    },
    {
        id: 'stimulus',
        title: 'กลุ่มกระตุ้นเศรษฐกิจและบริจาค',
        fields: [
            { id: 'easy_receipt', label: 'Easy E-Receipt (2568)', placeholder: 'สูงสุด 50,000', hint: 'ซื้อสินค้า 16 ม.ค. - 28 ก.พ. 68' },
            { id: 'home_loan', label: 'ดอกเบี้ยกู้ยืมเพื่อที่อยู่อาศัย', placeholder: 'สูงสุด 100,000', hint: 'ตามที่จ่ายจริง สูงสุด 100,000 บาท' },
            { id: 'donation_general', label: 'เงินบริจาคทั่วไป', placeholder: 'ระบุจำนวนเงิน', hint: 'ลดหย่อนได้ตามจริง ไม่เกิน 10% ของเงินได้สุทธิ' },
            { id: 'donation_education', label: 'เงินบริจาคการศึกษา/กีฬา/รพ.รัฐ', placeholder: 'ระบุจำนวนเงิน', hint: 'ลดหย่อนได้ 2 เท่า (ระบบจะคำนวณให้)' },
            { id: 'political_party', label: 'บริจาคพรรคการเมือง', placeholder: 'สูงสุด 10,000', hint: 'สูงสุด 10,000 บาท' },
        ]
    }
];
