# Technique leaves for the KS2 mind map: sub-group -> [(title, sign, key, [example problem ids])]
GROUP_VN = {
 1: ("Lý thuyết số", "Number Theory"),
 2: ("Chữ số & câu đố số", "Digits & Number Puzzles"),
 3: ("Số học, tỉ số & bài toán lời văn", "Arithmetic, Ratio & Word Problems"),
 4: ("Chuyển động & thời gian", "Motion, Rate & Time"),
 5: ("Hình học", "Geometry"),
 6: ("Tổ hợp & đếm", "Combinatorics & Counting"),
 7: ("Logic, trò chơi & tối ưu", "Logic, Games & Optimization"),
 8: ("Dãy số & quy luật", "Sequences, Patterns & Processes"),
}
SUB_VN = {
 "1.1": "Chia hết & số dư", "1.2": "Số nguyên tố, ước & số ước", "1.3": "ƯCLN, BCNN & chu kỳ", "1.4": "Chính phương & lũy thừa",
 "2.1": "Quan hệ giữa các chữ số", "2.2": "Phép tính ẩn chữ số", "2.3": "Đếm & cộng chữ số trên một dải", "2.4": "Lập số lớn nhất / nhỏ nhất",
 "3.1": "Tính nhanh", "3.2": "Tỉ số & phân số", "3.3": "Phần trăm", "3.4": "Trung bình cộng", "3.5": "Phương trình, tuổi, tiền",
 "4.1": "Gặp nhau & đuổi nhau", "4.2": "Vòng tròn & đồng hồ", "4.3": "Năng suất, dòng nước, nhiều chặng",
 "5.1": "Diện tích & tỉ số diện tích", "5.2": "Góc, tam giác & đa giác đều", "5.3": "Hình tròn & phần tô bóng", "5.4": "Hình chữ nhật, vuông, chu vi", "5.5": "Hình khối",
 "6.1": "Sắp xếp, chọn, chia", "6.2": "Đếm số theo điều kiện", "6.3": "Đếm hình trong lưới", "6.4": "Đường đi, lát, tô màu, đệ quy", "6.5": "Bắt tay & giải đấu",
 "7.1": "Suy luận & nói dối", "7.2": "Trò chơi lần lượt", "7.3": "Điền số vào sơ đồ", "7.4": "Cực trị, chuồng bồ câu, tối ưu",
 "8.1": "Dãy đều & vị trí", "8.2": "Dãy truy hồi & phép lặp", "8.3": "Quy luật hình phát triển",
}
L = {
"1.1": [
 ("Cùng số dư → ước của hiệu", "“chia cho cùng một số thì có số dư bằng nhau”", "Số chia d là ước của (a − b). Phân tích a − b ra thừa số rồi chọn ước thỏa điều kiện (ví dụ có 3 chữ số).", ["2003-13"]),
 ("Số dư kém số chia 1 đơn vị", "dư 1 khi chia 2, dư 2 khi chia 3, dư 3 khi chia 4…", "Khi đó x + 1 chia hết cho mọi số chia, tức x + 1 là bội của BCNN của chúng.", ["2007-5"]),
 ("Tìm thừa số để tích tận cùng cho trước", "“nhân với 123 để tích tận cùng là 2004”", "Xét lần lượt từ hàng đơn vị: chọn chữ số hàng đơn vị của x cho khớp chữ số cuối, rồi đến hàng chục, hàng trăm…", ["2004-4", "2009-1"]),
 ("Dấu hiệu chia hết & số ghép", "bội của 4, 6, 28, 99…; số chỉ gồm chữ số 4 và 6", "4: hai chữ số cuối; 3 và 9: tổng chữ số; 11: hiệu tổng chữ số ở vị trí lẻ và chẵn. Số chia là hợp số thì tách thành các thừa số nguyên tố cùng nhau (28 = 4 × 7).", ["2003-14", "2011-10", "2021-3", "2026-12"]),
 ("Hệ điều kiện về số dư", "chia 3, 5, 11 lần lượt dư 0, 1, 3", "Liệt kê các số thỏa điều kiện của số chia lớn nhất, rồi thử dần các điều kiện còn lại. Các nghiệm lặp lại sau mỗi BCNN.", ["2016-14", "2015-12"]),
 ("Nhân đôi số → biến đổi số dư", "“dư 26; nhân đôi rồi chia thì dư 7”", "2n có số dư 2 × 26 = 52 thu gọn về 7, nên d là ước của 52 − 7 = 45. Nhớ điều kiện số chia lớn hơn số dư.", ["2024-4"]),
 ("Tổng phải chia hết", "bỏ một hộp thì phần còn lại có xanh gấp 3 lần đỏ", "Phần còn lại phải chia hết cho 1 + 3 = 4. Xét số dư khi chia 4 của tổng và của từng hộp.", ["2004-3", "2012-13"]),
 ("Chữ số tận cùng của tích", "“bỏ ít thừa số nhất để tích tận cùng là 9”", "Chỉ cần theo dõi chữ số cuối. Bỏ các thừa số chẵn và các thừa số chứa 5 (vì chúng tạo số 0 ở cuối), rồi điều chỉnh để chữ số cuối là 9.", ["2013-12"]),
 ("Số có cấu trúc lặp", "abcdef − defabc, abcabc", "abcabc = abc × 1001 = abc × 7 × 11 × 13. abcdef − defabc = 999 × (abc − def).", ["2010-8"]),
 ("Đếm bội số trong một khoảng", "“có bao nhiêu bội của 18 nằm giữa …”", "Số bội của k trong đoạn [a, b] bằng ⌊b/k⌋ − ⌊(a−1)/k⌋.", ["2016-4"]),
],
"1.2": [
 ("Đếm số ước", "“có đúng 16 ước”, “cùng số ước với 2015”", "n = p^a · q^b · … thì số ước là (a+1)(b+1)… Muốn n nhỏ nhất thì đặt số mũ lớn cho số nguyên tố nhỏ.", ["2008-7", "2015-1", "2019-9", "2026-14"]),
 ("Phân tích ra thừa số rồi chia phần", "tích của các số bằng 2014 hoặc 360", "Phân tích ra thừa số nguyên tố (2014 = 2 · 19 · 53; 360 = 2³ · 3² · 5), rồi liệt kê mọi cách chia các thừa số vào các số.", ["2014-6", "2018-10", "2009-6", "2023-3", "2009-2"]),
 ("Số nguyên tố & chẵn lẻ", "tổng hoặc hiệu các số nguyên tố, p + q = r", "Mọi số nguyên tố trừ 2 đều lẻ. Vì vậy p + q = r buộc một số phải là 2. Với tổng bình phương, xét thêm số dư khi chia cho 3.", ["2007-14", "2025-15", "2009-3", "2015-11"]),
 ("Giữ đủ lũy thừa nguyên tố", "“tích còn lại chia hết cho 1, 2, …, 15”", "Tích phải chứa đủ 2³, 3², 5, 7, 11, 13. Bỏ được mọi số còn lại miễn là vẫn giữ đủ các lũy thừa này.", ["2022-14", "2024-2"]),
],
"1.3": [
 ("Sự kiện lặp → BCNN", "hai người nghỉ cùng ngày, biển quảng cáo quay vòng", "Hai chu kỳ a và b trùng nhau sau mỗi BCNN(a, b) đơn vị thời gian. Với hoán vị thì lấy BCNN của độ dài các vòng.", ["2006-12", "2010-1", "2013-3"]),
 ("Bao hàm – loại trừ với bội số", "vết cắt trùng nhau, dấu chân trên bậc thang", "|A ∪ B| = |A| + |B| − |A ∩ B|. Phần trùng nhau là các bội của BCNN.", ["2017-2", "2005-7"]),
 ("Tính chất của ƯCLN", "phân số tối giản a/b với a + b = 333; ƯCLN lớn nhất của 25 số có tổng 2016", "ƯCLN(a, b) = ƯCLN(a, a + b). Nếu d là ước của từng số trong n số thì d là ước của tổng và n·d ≤ tổng.", ["2005-6", "2016-9", "2011-7", "2017-6"]),
],
"1.4": [
 ("Điều kiện để là số chính phương hoặc lập phương", "bỏ ít số nhất để tích là số chính phương", "n là số chính phương khi mọi số mũ trong phân tích đều chẵn; là lập phương khi mọi số mũ chia hết cho 3.", ["2007-10", "2013-8", "2013-13", "2005-2", "2014-1"]),
 ("Chữ số tận cùng của số chính phương", "“ba chữ số cuối giống nhau”", "Số chính phương chỉ tận cùng bằng 0, 1, 4, 5, 6, 9. Thu hẹp dần bằng số dư khi chia 4, 8, 1000.", ["2009-9"]),
 ("Tổng lũy thừa của 2 và 3", "biểu diễn thành 2^a + 3^b", "Liệt kê sẵn: 2 → 1, 2, 4, …, 512; 3 → 1, 3, 9, 27, 81, 243, 729. Lọc theo chữ số tận cùng.", ["2013-6", "2021-10"]),
],
"2.1": [
 ("Viết số dưới dạng 10a + b", "đảo ngược chữ số, “gấp 3 lần”, “bằng 4⅓ tổng chữ số”", "Số ab = 10a + b, số đảo ba = 10b + a. Hiệu của chúng là 9(a − b), tổng là 11(a + b).", ["2003-6", "2003-8", "2011-12", "2007-4"]),
 ("Tổng chữ số khi cộng có nhớ", "“cộng 4 thì tổng chữ số giảm một nửa”", "Mỗi lần nhớ làm tổng chữ số giảm 9: S(n + k) = S(n) + k − 9 × (số lần nhớ).", ["2012-3", "2015-10", "2016-12"]),
 ("Hiệu khi sắp lại chữ số", "số lớn nhất trừ số nhỏ nhất tạo từ ba chữ số", "abc − cba = 99(a − c), nên kết quả là bội của 99.", ["2009-8"]),
],
"2.2": [
 ("Giải mã phép tính chữ cái", "mỗi chữ cái là một chữ số khác nhau", "Bắt đầu ở cột đơn vị và chữ số đầu tiên (số nhớ chỉ là 0, 1 hoặc 2). Dùng số dư khi chia 9 (tổng chữ số) để kiểm tra.", ["2008-13", "2019-15", "2018-7", "2022-12", "2026-13"]),
 ("Phân tích tích có cấu trúc", "abc × cba = 396396; ACCC = 2/5 · CCCB", "Phân tích ra thừa số nguyên tố rồi ghép lại: 396396 = 396 × 1001 = 2² · 3² · 7 · 11² · 13.", ["2007-1", "2008-10", "2018-4"]),
 ("Điền các chữ số 1–9 vào ô", "dùng mỗi chữ số đúng một lần", "Tổng 1 + 2 + … + 9 = 45. Xét số dư khi chia 9 và đặt chữ số lớn vào hàng cao.", ["2015-6", "2018-6", "2024-7", "2024-8", "2025-10"]),
],
"2.3": [
 ("Đếm chữ số theo nhóm độ dài", "chữ số thứ 2005 của dãy 123456789101112…", "Số 1 chữ số dùng 9 chữ số, số 2 chữ số dùng 180, số 3 chữ số dùng 2700. Trừ dần để biết đang ở số nào.", ["2005-10", "2019-13", "2017-12"]),
 ("Tổng hoặc tích chữ số trên một khoảng", "cộng tích các chữ số từ 1 đến 2025", "Với 0–999, mỗi chữ số xuất hiện đều nhau ở mỗi hàng. Tổng các tích chữ số của số k chữ số bằng (1 + 2 + … + 9)^k = 45^k.", ["2025-7", "2013-7", "2010-2"]),
],
"2.4": [
 ("Tham lam từ hàng cao nhất", "tích lớn nhất, xóa 7 chữ số để được số lớn nhất", "Chọn chữ số lớn nhất có thể cho hàng cao nhất, rồi đến hàng tiếp theo. Muốn tích hai số lớn nhất thì hai số nên gần bằng nhau.", ["2003-15", "2016-11", "2018-8", "2010-15"]),
],
"3.1": [
 ("Tổng xen kẽ các bình phương", "1² − 2² + 3² − 4² + …", "Ghép cặp: (n+1)² − n² = 2n + 1. Với n lẻ, 1² − 2² + … + n² = n(n+1)/2.", ["2003-9", "2004-12"]),
 ("Số lặp khối", "200320032003 × 2004200420042004 − …", "Tách 200320032003 = 2003 × 100010001; hai vế thường có chung nhân tử nên hiệu bằng 0. 99…98 × 100…02 = 10^(2n) − 4.", ["2004-2", "2014-12"]),
 ("Phép toán tự định nghĩa và biểu thức dài", "a ∗ b là …; phần nguyên của A", "Tính vài bước đầu để tìm quy luật. Với tổng dài, tìm cách triệt tiêu từng cặp (rút gọn liên tiếp).", ["2011-1", "2011-3", "2007-8", "2022-10", "2024-5", "2026-3"]),
],
"3.2": [
 ("Biểu diễn theo phần bằng nhau", "A nhiều hơn B 80%, B : C = 7 : 5", "Chọn một đơn vị chung (BCNN các mẫu số), rồi viết mỗi đại lượng thành số phần.", ["2007-9", "2003-4", "2005-14", "2004-8"]),
 ("Chuỗi tỉ lệ trao đổi", "11 dừa = 14 dứa, 22 xoài = 21 dứa…", "Nhân các tỉ lệ nối tiếp nhau: dừa/cam = (dừa/dứa) × (dứa/xoài) × (xoài/chuối) × (chuối/cam).", ["2011-2", "2005-3"]),
 ("Phân số nằm giữa hai phân số", "nhiều hơn 2/5 nhưng ít hơn 1/2", "Thử n = 1, 2, 3, … đến khi có số nguyên nằm giữa (2/5)n và (1/2)n. Với phương trình phân số, đặt ẩn cho tử và mẫu.", ["2014-2", "2021-4", "2024-1", "2014-4"]),
 ("Tổng nghịch đảo bằng 1", "1/a + 1/b + 1/c = 1", "Chỉ có ba bộ nghiệm: (3, 3, 3), (2, 4, 4) và (2, 3, 6).", ["2017-1"]),
],
"3.3": [
 ("Gọi tổng là 100 phần", "“nhiều hơn 22% so với ban đầu”", "Tăng 22% nghĩa là nhân với 1,22. Đặt tổng ban đầu bằng 100 phần rồi tính từng bước.", ["2003-2", "2003-11", "2008-3"]),
 ("Tối thiểu cùng tham gia (lấy phần bù)", "80% chơi bóng rổ, 85% chơi bóng đá… ít nhất bao nhiêu % chơi cả bốn môn", "Cộng tỉ lệ không tham gia của từng môn. Số tham gia cả bốn môn ít nhất bằng 100% trừ tổng đó.", ["2004-9"]),
 ("Phần trăm của hai nhóm", "lớp 5 có 9%, lớp 6 có 11%…", "Đặt ẩn cho số lượng mỗi nhóm, rồi cho hai đại lượng bằng nhau để lập phương trình.", ["2019-4", "2012-11"]),
],
"3.4": [
 ("Làm việc với tổng, không với trung bình", "bỏ một số thì trung bình còn 6,1", "Tổng = trung bình × số phần tử. Thêm hoặc bớt phần tử thì tính sự thay đổi của tổng.", ["2004-1", "2006-3", "2006-5", "2019-5", "2025-5"]),
 ("Trộn nhóm: độ lệch triệt tiêu", "trung bình của nam, của nữ và của cả lớp", "n₁(m₁ − m) + n₂(m₂ − m) = 0, trong đó m là trung bình chung của cả hai nhóm.", ["2022-3", "2022-7", "2025-9", "2015-8"]),
],
"3.5": [
 ("Bài toán tuổi", "khi A 8 tuổi thì bố 31 tuổi…", "Hiệu số tuổi không đổi theo thời gian. Đặt ẩn là tuổi hiện tại.", ["2006-1", "2012-15"]),
 ("Hệ hai đại lượng (gà – chó)", "3 vịt + 2 vịt con = 32 kg; số chân và số đầu", "Cộng hoặc trừ hai phương trình để khử một ẩn. Hoặc giả sử tất cả cùng một loại rồi tính phần chênh lệch.", ["2008-2", "2014-3", "2014-10", "2016-5", "2006-11"]),
 ("Thay đổi giá và số lượng", "bán thêm 10 quả thì giá mỗi quả giảm 2", "Gọi số lượng là n, giá là p: (n + 10)(p − 2) = np = (n − 10)(p + 4).", ["2003-1", "2010-4", "2014-7", "2016-7"]),
 ("Các tổng “bỏ đi một số”", "tổng của 9 trong 10 số; tổng hai người ngồi cạnh", "Cộng tất cả các tổng lại: mỗi số được đếm (n − 1) lần (hoặc 2 lần với hai người kề nhau).", ["2005-12", "2025-2"]),
],
"4.1": [
 ("Đi ngược chiều gặp nhau", "hai người xuất phát từ hai đầu", "Thời gian gặp = khoảng cách / (v₁ + v₂). Nếu một người đi trước thì trừ phần quãng đường đã đi trước đó.", ["2003-3", "2006-7", "2021-5"]),
 ("Sau khi gặp còn đi t₁ và t₂ giờ", "sau khi gặp, xe A mất 5 giờ, xe B mất 7,2 giờ", "v₁ / v₂ = √(t₂ / t₁).", ["2005-11", "2007-11"]),
 ("Gặp nhau nhiều lần", "quay đầu lại, gặp lần thứ ba", "Giữa hai lần gặp liên tiếp, tổng quãng đường hai người đi bằng 2 lần khoảng cách.", ["2009-10"]),
 ("Đuổi kịp, vượt xe, chạy đua", "xe con vượt xe tải; khi A về đích thì B còn cách 40 m", "Vận tốc tương đối = v₁ − v₂, quãng cần vượt = tổng chiều dài hai xe. Trong đua, tỉ số quãng đường = tỉ số vận tốc.", ["2008-4", "2016-2", "2026-1", "2021-6"]),
],
"4.2": [
 ("Chạy trên đường vòng", "chạy ngược chiều trên đường tròn 400 m", "Ngược chiều thì gặp nhau sau mỗi L/(v₁ + v₂). Cùng chiều thì sau mỗi L/(v₁ − v₂).", ["2007-7", "2023-8", "2004-11"]),
 ("Kim đồng hồ", "giữa 4:00 và 5:00 hai kim lệch nhau 10°", "Kim phút quay 6°/phút, kim giờ 0,5°/phút, nên khoảng cách thay đổi 5,5°/phút.", ["2011-4"]),
 ("Đường khép kín lặp lại", "kiến đi theo hình số 8 được 2005π", "Lấy tổng quãng đường chia lấy dư cho độ dài một vòng.", ["2005-8"]),
],
"4.3": [
 ("Vòi chảy vào và chảy ra", "thuyền bị thủng nhưng có máy bơm", "Tốc độ thực = tốc độ vào − tốc độ ra. Thời gian = giới hạn / tốc độ thực.", ["2003-5", "2015-5"]),
 ("Xuôi ngược dòng, lên xuống dốc", "dòng nước 1 km/h; lên dốc 4 km/h, xuống dốc 6 km/h", "v_xuôi = v + c, v_ngược = v − c. Đường có dốc: lượt về đổi lên dốc thành xuống dốc, nên lập hệ hai phương trình thời gian.", ["2010-6", "2014-14"]),
 ("Cùng quãng đường, khác vận tốc", "chạy gấp đôi vận tốc đi bộ", "Cùng quãng đường thì thời gian tỉ lệ nghịch với vận tốc. Tách thành từng chặng.", ["2016-6", "2005-9"]),
],
"5.1": [
 ("Tam giác cùng chiều cao", "điểm trên cạnh chia theo tỉ lệ cho trước", "Hai tam giác chung đỉnh, có đáy nằm trên cùng một đường thẳng thì tỉ số diện tích bằng tỉ số hai đáy.", ["2003-10", "2007-2", "2016-10", "2024-10"]),
 ("Trung điểm trong hình bình hành / hình chữ nhật", "trung điểm, AM = 2MD, diện tích hình bình hành là 60", "Tam giác có đáy là một cạnh và đỉnh nằm trên cạnh đối diện bằng ½ hình bình hành. Kẻ thêm đường phụ để chia hình thành các phần bằng nhau.", ["2008-9", "2010-10", "2018-13", "2019-10", "2024-9", "2026-8"]),
 ("Hai đoạn thẳng cắt nhau (mô hình con bướm)", "BE và CF cắt nhau tại G", "Trong hình thang, hai tam giác ở hai bên bằng nhau. Giao điểm chia đoạn thẳng theo tỉ số hai đáy song song.", ["2012-5", "2015-13", "2021-8", "2012-14"]),
 ("Lục giác đều và tam giác đều", "lục giác đều ABCDEF", "Lục giác đều gồm 6 tam giác đều. Chia nhỏ thành các tam giác đơn vị rồi đếm.", ["2007-13", "2007-15", "2022-1"]),
 ("Dời hình để tính phần tô bóng", "tỉ số phần tô bóng / phần trắng", "Xoay, trượt hoặc lật các mảnh để ghép thành hình quen thuộc. Dùng đối xứng để so sánh các phần.", ["2003-7", "2013-4", "2019-1", "2025-1", "2025-8"]),
],
"5.2": [
 ("Tổng góc", "tìm x, tính a + b + c", "Tổng ba góc tam giác là 180°, tổng góc n-giác là (n − 2) · 180°. Góc ngoài bằng tổng hai góc trong không kề với nó.", ["2004-14", "2004-15", "2006-9"]),
 ("Tìm tam giác cân ẩn", "AP = AQ, AB = CD", "Hai cạnh bằng nhau thì hai góc đáy bằng nhau. Tìm các cặp đoạn bằng nhau để phát hiện tam giác cân.", ["2011-13", "2021-13", "2022-13"]),
 ("Đa giác đều", "8 hình thang ghép thành bát giác đều", "Góc ở tâm của n-giác đều là 360°/n, mỗi góc trong là 180° − 360°/n.", ["2010-7", "2021-14", "2011-11"]),
 ("Bất đẳng thức tam giác và Pythagore", "AC là số nguyên; trung tuyến vuông góc", "|a − b| < c < a + b, áp dụng cho cả hai tam giác chung cạnh. Định lý Pythagore: a² + b² = c². Trọng tâm chia trung tuyến theo tỉ số 2 : 1.", ["2010-5", "2013-10", "2019-11", "2025-11"]),
],
"5.3": [
 ("Hình tròn: cộng rồi trừ phần chồng lấn", "nửa hình tròn và phần tư hình tròn chồng lên tam giác", "Diện tích viên phân = hình quạt − tam giác. Tính tổng các hình rồi trừ đi phần bị đếm hai lần.", ["2009-7", "2016-3", "2008-11", "2019-2"]),
 ("Phần chung triệt tiêu", "hiệu diện tích phần tô và phần trắng", "Khi hai vùng có chung phần chồng lấn, hiệu diện tích của chúng bằng hiệu diện tích hai hình lớn, không cần tính phần chung.", ["2006-15", "2009-12", "2023-1", "2024-12", "2026-5"]),
 ("Vùng bao quanh đa giác", "hươu ăn cỏ cách hàng rào tối đa 2 m", "Vùng này gồm các hình chữ nhật dọc mỗi cạnh, cộng các hình quạt ở các đỉnh. Các hình quạt ghép lại đúng thành một hình tròn bán kính r.", ["2007-6", "2012-4"]),
],
"5.4": [
 ("Cộng các phép đo", "hai người, mỗi người đo ba cạnh của hình chữ nhật", "(2a + b) + (a + 2b) = 3(a + b), từ đó suy ra chu vi.", ["2006-2"]),
 ("Hình vuông nghiêng trên lưới", "đỉnh hình vuông nằm trên các điểm lưới", "Hình vuông nghiêng có cạnh ứng với độ dịch (a, b) có diện tích a² + b² và chiếm một khung (a + b) × (a + b).", ["2012-7"]),
 ("Đường ngắn nhất bằng phép đối xứng", "PE + PC nhỏ nhất, P chạy trên đường chéo", "Lấy đối xứng một điểm qua đường thẳng rồi nối thẳng. Đường chéo hình vuông là trục đối xứng có sẵn.", ["2015-7", "2014-8"]),
 ("Cắt ghép hình chữ nhật", "ghép lại thành hình chữ nhật, hai hình vuông chồng nhau", "Cắt ghép không làm đổi diện tích. Dùng ước của diện tích để tìm kích thước có thể có.", ["2015-3", "2022-4", "2014-11", "2009-4"]),
],
"5.5": [
 ("Khối lập phương sơn rồi cắt", "khối 4 × 5 × 6 sơn đỏ rồi cắt thành khối 1 cm", "Có 8 khối sơn 3 mặt (ở các góc). Số khối sơn 2 mặt là 4[(a−2) + (b−2) + (c−2)].", ["2007-3", "2015-9"]),
 ("Hình khai triển và công thức Euler", "hình khai triển của đa diện", "Đỉnh − Cạnh + Mặt = 2. Mỗi cạnh là cạnh chung của đúng 2 mặt.", ["2009-11"]),
 ("Cuộn thành hình trụ", "cuộn tờ giấy theo hai chiều khác nhau", "Chu vi đáy = cạnh được cuộn − phần chồng mép. V = πr²h.", ["2010-11"]),
],
"6.1": [
 ("Chia kẹo (que và sao)", "20 bút chì giống nhau chia cho 3 bạn, mỗi bạn ít nhất 1", "Chia n vật giống nhau cho k người, mỗi người ít nhất 1 vật: C(n − 1, k − 1) cách.", ["2012-1"]),
 ("Lấy phần bù", "ít nhất 2 bạn nữ; hai số kề nhau không chênh 3", "Đếm tất cả các trường hợp rồi trừ các trường hợp vi phạm.", ["2014-5", "2017-10"]),
 ("Thứ tự từ điển", "số thứ 502; vị trí của từ DURBAN", "Cố định chữ số hoặc chữ cái đầu: mỗi lựa chọn ứng với (n − 1)! hoán vị. Trừ dần để tìm vị trí.", ["2008-5", "2019-12"]),
 ("Trả tiền bằng các mệnh giá", "trả 500 đô bằng tờ 10, 20, 50", "Cố định số tờ mệnh giá lớn nhất, rồi đếm số cách cho phần còn lại.", ["2011-6"]),
 ("Xếp chỗ có ràng buộc", "hai người lớn không ngồi cạnh nhau; Bob ngồi bên trái Alice", "Xếp nhóm tự do trước rồi chèn nhóm bị ràng buộc vào các khe. Nếu k người phải theo một thứ tự cố định thì chia cho k!.", ["2025-12", "2015-15"]),
],
"6.2": [
 ("Nhân số lựa chọn theo từng vị trí", "chữ số đầu + chữ số cuối = 13", "Nhân số lựa chọn của từng vị trí. Chữ số đầu tiên không được bằng 0.", ["2006-6", "2017-9", "2023-4"]),
 ("Chữ số giảm dần tương ứng chọn tập con", "chữ số giảm dần; số hình chữ V", "Mỗi số có các chữ số giảm dần ứng với một cách chọn k chữ số khác nhau, nên có C(10, k) số.", ["2004-10", "2025-14"]),
 ("Có ít nhất một chữ số 3", "bội của 3 có ít nhất một chữ số 3", "Đếm tất cả rồi trừ đi các số không chứa chữ số 3.", ["2008-8"]),
 ("Biểu diễn nhị phân", "tổng của đúng 9 lũy thừa khác nhau của 2", "Mỗi số có đúng một biểu diễn nhị phân. Số lũy thừa được dùng bằng số chữ số 1 trong biểu diễn đó.", ["2013-9"]),
],
"6.3": [
 ("Đếm hình chữ nhật trong lưới m × n", "có bao nhiêu hình chữ nhật", "Chọn 2 trong m + 1 đường dọc và 2 trong n + 1 đường ngang: C(m+1, 2) × C(n+1, 2).", ["2018-12", "2026-7", "2011-9", "2017-11"]),
 ("Đếm hình vuông, kể cả hình nghiêng", "hình vuông có đỉnh là các điểm của lưới", "Lưới n × n có tổng k² hình vuông thẳng. Mỗi khung k × k còn chứa thêm k − 1 hình vuông nghiêng.", ["2013-5", "2013-14"]),
 ("Đường chéo cắt qua lưới", "đường chéo hình chữ nhật 24 × 60 chia thành bao nhiêu phần", "Số ô đường chéo đi qua trong hình a × b là a + b − ƯCLN(a, b).", ["2021-11"]),
],
"6.4": [
 ("Bậc thang 1 hoặc 2 bước (Fibonacci)", "mỗi lần lên 1 hoặc 2 bậc; không có hai chữ số 3 kề nhau", "f(n) = f(n − 1) + f(n − 2). Nếu có bậc bị hỏng thì chia thành các đoạn và nhân kết quả.", ["2009-13", "2008-6"]),
 ("Tô màu sao cho hai vùng kề khác màu", "5 màu, hai hình tròn được nối phải khác màu", "Tô vùng có nhiều vùng kề nhất trước, rồi nhân số lựa chọn còn lại của từng vùng.", ["2009-15", "2018-11", "2014-15"]),
 ("Đếm đường đi trên sơ đồ", "đi từ ô trung tâm, đi qua các viên gạch", "Số cách đến một điểm bằng tổng số cách đến các điểm ngay trước nó.", ["2008-1", "2019-14"]),
 ("Lát gạch và chia hình", "dùng tetromino, chia hình thành hai phần giống nhau", "Tô màu ô cờ để kiểm tra khả năng lát. Xét đối xứng khi chia hình.", ["2021-2", "2022-6", "2025-13"]),
 ("Nối điểm không cắt nhau (Catalan)", "6 điểm trên đường tròn, các đoạn không cắt nhau", "Số cách nối 2n điểm trên đường tròn thành các đoạn không cắt nhau là số Catalan: 1, 2, 5, 14, …", ["2024-15"]),
 ("Chia nhóm theo số dư", "chia 1..12 thành các bộ ba có tổng chia hết cho 3", "Phân loại các số theo số dư khi chia 3, rồi đếm các cách ghép phù hợp.", ["2015-14"]),
],
"6.5": [
 ("Bắt tay", "tổng số lần bắt tay là 2014", "n người bắt tay từng đôi một có n(n − 1)/2 lần bắt tay. Tìm n cho tổng gần nhất rồi điều chỉnh.", ["2014-9", "2026-4"]),
 ("Giải đấu vòng tròn", "mỗi cặp đấu với nhau đúng một trận, không có trận hòa", "Số trận là C(n, 2). Mỗi trận có đúng một người thắng, nên tổng số trận thắng bằng số trận.", ["2008-12"]),
 ("Đồ thị: đếm theo bậc", "mỗi người có 1 hoặc 2 bạn; mỗi làng giáp 3 làng", "Tổng các bậc = 2 × số cạnh, nên số đỉnh có bậc lẻ luôn là số chẵn.", ["2012-6", "2024-13"]),
],
"7.1": [
 ("Người nói thật và người nói dối", "ba người không bao giờ nói dối", "Xét từng giả thiết rồi tìm mâu thuẫn. Hai câu nói trái ngược nhau thì không thể cùng đúng.", ["2004-13", "2026-2"]),
 ("Bảng suy luận", "ba người giữ ba chức vụ khác nhau", "Kẻ bảng người × chức vụ, đánh dấu loại dần từng ô.", ["2006-13"]),
],
"7.2": [
 ("Lấy lần lượt 1, 2, 3, 4, …", "cuối cùng John có 1012 viên kẹo", "Sau k lượt của mỗi người, người đi trước có 1 + 3 + 5 + … = k², người đi sau có 2 + 4 + … = k(k + 1). Tìm k rồi xử lý riêng lượt cuối.", ["2004-7", "2025-3", "2011-5"]),
],
"7.3": [
 ("Tổng bằng nhau: đếm ô chung nhiều lần", "các cạnh có tổng bằng nhau; tìm số ở giữa", "Cộng tổng của tất cả các cạnh: các ô chung được đếm nhiều lần. Từ đó tìm được tổng mỗi cạnh và số ở ô trung tâm.", ["2005-15", "2010-13", "2018-3", "2024-6", "2022-8", "2021-9"]),
],
"7.4": [
 ("Chuồng bồ câu (trường hợp xấu nhất)", "cần rút ít nhất bao nhiêu quả để chắc chắn…", "Tính số quả lớn nhất có thể rút mà vẫn chưa đạt yêu cầu, rồi cộng thêm 1.", ["2007-12"]),
 ("Sắp xếp công việc tối ưu", "rán 5 con cá; lấy 600 g đường bằng cân", "Đừng để chảo hay cân trống. Tách nhỏ công việc và luân phiên các phần.", ["2004-6", "2004-5", "2016-1"]),
 ("Các số khác nhau: ít nhất bao nhiêu số lẻ", "49 số khác nhau có tổng 2016", "So sánh với tổng nhỏ nhất (1 + 2 + … + n) và xét tính chẵn lẻ của tổng.", ["2012-8", "2016-8"]),
 ("Chia đều để tối ưu", "tích lớn nhất trong các nhóm nhỏ nhất có thể", "Muốn giá trị lớn nhất nhỏ nhất thì chia các phần càng đều càng tốt. Kiểm tra các trường hợp biên.", ["2019-8", "2022-11", "2026-6", "2021-1"]),
],
"8.1": [
 ("Cấp số cộng", "4, 7, 10, 13, …; 23 số lẻ liên tiếp", "aₙ = a₁ + (n − 1)d. Số số hạng = (số cuối − số đầu)/d + 1.", ["2005-1", "2010-12", "2019-3", "2024-14"]),
 ("Vị trí trong chu kỳ", "trạm thu phí trên đường vòng; nhà đối diện nhau", "Lấy số dư theo độ dài một chu kỳ để biết vị trí.", ["2012-2", "2006-4"]),
 ("Dãy theo hệ cơ số đặc biệt", "số “tốt” thứ 100; cạnh mỗi hình vuông bằng đường chéo hình trước", "Dãy tương ứng với một hệ cơ số (có thể là hệ cơ số hỗn hợp): đổi thứ tự n sang hệ đó. Cạnh nhân √2 sau mỗi bước.", ["2013-15", "2013-1"]),
],
"8.2": [
 ("Dãy lặp: tìm chu kỳ", "số hạng thứ 2009 chia 8 dư bao nhiêu; lập phương các chữ số", "Tính các số hạng đến khi thấy lặp lại. Ví dụ, dãy Fibonacci khi chia cho 8 lặp lại sau mỗi 12 số hạng.", ["2009-5", "2017-8", "2023-12", "2026-9"]),
],
"8.3": [
 ("Hình phát triển theo bước", "hình vuông thứ 2005 hơn hình thứ 2004 bao nhiêu viên", "Đếm với n = 1, 2, 3, 4, tìm hiệu giữa các bước rồi lập công thức (thường có dạng n²).", ["2005-13", "2006-14", "2011-14"]),
 ("Xoắn ốc trên lưới", "số 2008 nằm ở hàng nào, cột nào; ô cuối của con ốc", "Các số ở góc xoắn ốc thường là số chính phương hoặc số tam giác. Xác định vòng chứa số cần tìm.", ["2008-14", "2011-15", "2026-11"]),
],
}


# ---- Team-paper additions --------------------------------------------------
# Leaf ids ("1.1-a") key the saved progress in the page, so new leaves are only ever
# appended at the end of a sub-group; team problems are added as extra examples.
TEAM_EXAMPLES = {
 "1.1-a": ["2003-T7", "2006-T8"], "1.1-d": ["2017-T3", "2014-T5"],
 "1.2-a": ["2016-T5", "2025-T3", "2025-T7", "2026-T2"], "1.2-b": ["2004-T4", "2007-T8"], "1.2-c": ["2007-T5"],
 "1.3-a": ["2009-T3"], "1.3-c": ["2004-T3", "2018-T10", "2007-T9"],
 "1.4-a": ["2023-T6", "2025-T1"],
 "2.1-a": ["2004-T1", "2006-T3", "2008-T1", "2017-T10"], "2.1-b": ["2007-T4"],
 "2.2-a": ["2017-T2", "2005-T9", "2004-T8", "2011-T8"], "2.2-c": ["2013-T9"],
 "2.3-a": ["2007-T2", "2024-T2"], "2.3-b": ["2005-T4"],
 "2.4-a": ["2006-T2", "2015-T9", "2010-T6", "2022-T4"],
 "3.1-c": ["2004-T5", "2004-T7", "2014-T1", "2008-T4", "2013-T2"],
 "3.2-a": ["2012-T4", "2021-T7"], "3.3-a": ["2003-T5", "2024-T1"], "3.4-a": ["2006-T5", "2021-T4", "2022-T6"],
 "3.5-b": ["2007-T7", "2010-T5", "2019-T1", "2012-T5", "2003-T2"],
 "4.1-c": ["2008-T3", "2023-T3"], "4.1-d": ["2015-T4", "2018-T8", "2021-T10"],
 "4.2-b": ["2024-T3"], "4.3-a": ["2011-T4"], "4.3-b": ["2007-T1"],
 "5.1-a": ["2003-T1", "2016-T4", "2024-T4", "2013-T4"], "5.1-b": ["2003-T3", "2006-T4", "2007-T3", "2026-T5", "2025-T5"],
 "5.1-e": ["2005-T1", "2005-T2", "2019-T2", "2017-T7", "2009-T7"],
 "5.2-a": ["2008-T2", "2012-T8"], "5.2-b": ["2015-T8", "2023-T8", "2024-T6", "2026-T8"],
 "5.3-a": ["2003-T8", "2009-T8", "2026-T1"], "5.3-b": ["2015-T5"],
 "5.4-d": ["2017-T1", "2018-T7", "2022-T8", "2014-T3", "2012-T6"],
 "5.5-a": ["2006-T6", "2009-T2"],
 "6.1-b": ["2003-T9"], "6.1-e": ["2004-T6", "2019-T5", "2022-T10"],
 "6.2-a": ["2015-T10", "2016-T7", "2021-T8", "2022-T5", "2011-T6"], "6.2-c": ["2003-T10"],
 "6.3-b": ["2014-T6", "2023-T10"],
 "6.4-a": ["2006-T10"], "6.4-b": ["2023-T4", "2026-T10", "2016-T2", "2013-T3"], "6.4-c": ["2011-T5", "2021-T1", "2009-T9"],
 "6.4-d": ["2016-T8", "2013-T8", "2010-T10", "2009-T4", "2025-T4"],
 "6.5-b": ["2014-T7", "2022-T7"],
 "7.1-b": ["2014-T4", "2015-T6", "2018-T1", "2019-T6", "2011-T9"],
 "7.3-a": ["2004-T10", "2005-T5", "2005-T7", "2008-T9", "2009-T10", "2012-T1", "2012-T9", "2013-T7", "2017-T6", "2017-T8", "2010-T9"],
 "7.4-b": ["2014-T10", "2015-T3", "2010-T2", "2024-T8", "2019-T3"], "7.4-d": ["2013-T6", "2008-T7", "2022-T9", "2025-T2"],
 "8.1-a": ["2009-T1", "2024-T5"], "8.1-b": ["2012-T2", "2012-T3"],
 "8.2-a": ["2011-T2", "2012-T10", "2014-T9", "2017-T9", "2019-T10", "2022-T1", "2026-T3"],
 "8.3-a": ["2010-T1", "2018-T5", "2023-T9"], "8.3-b": ["2009-T6", "2022-T3"],
}
NEW_LEAVES = {
"1.1": [("Số chữ số 0 ở cuối n!", "“có bao nhiêu chữ số 0 ở cuối 1 × 2 × … × 2003”", "Mỗi chữ số 0 cần một cặp 2 × 5, mà thừa số 5 luôn ít hơn thừa số 2. Số chữ số 0 = ⌊n/5⌋ + ⌊n/25⌋ + ⌊n/125⌋ + …", ["2003-T4"])],
"1.2": [("Tổng các số nguyên dương liên tiếp", "“có bao nhiêu cách viết 270 thành tổng các số liên tiếp”", "Tổng k số liên tiếp bắt đầu từ a bằng k(2a + k − 1)/2. Số cách viết N thành tổng của ít nhất hai số nguyên dương liên tiếp bằng số ước lẻ của N trừ 1.", ["2007-T10", "2011-T10"])],
"1.4": [("Tổng hai số chính phương và hệ nhị phân", "tổng hai số chính phương; gói 1, 2, 4, 8, … bút", "Số chính phương chia 4 dư 0 hoặc 1, nên tổng hai số chính phương không bao giờ có dạng 4k + 3. Mỗi số tự nhiên viết được duy nhất thành tổng các lũy thừa khác nhau của 2.", ["2017-T4", "2019-T4"])],
"4.3": [("Cỏ mọc đều (bài toán Newton)", "cỏ vẫn mọc trong lúc bò ăn; nước vẫn rò trong lúc bơm", "Lượng ban đầu + tốc độ mọc × t = số con × tốc độ ăn × t. Lập hai phương trình từ hai tình huống để tìm tốc độ mọc và lượng ban đầu.", ["2026-T9", "2009-T5"])],
"5.4": [("Phản xạ (bi-a, tia sáng)", "bóng nảy trên bàn bi-a", "Lấy đối xứng bàn qua các cạnh để duỗi thẳng đường đi: đường gấp khúc trở thành một đoạn thẳng trên lưới các bàn đối xứng.", ["2019-T8"])],
"5.5": [("Diện tích bề mặt và đếm khối lập phương", "dán ba khối lập phương; tháp có lỗ xuyên qua", "Diện tích bề mặt = tổng diện tích các khối − 2 × diện tích các mặt dán nhau. Đếm khối theo từng tầng, hoặc đếm mặt nhìn thấy theo 6 hướng.", ["2004-T2", "2006-T7", "2021-T6", "2023-T7", "2003-T6"])],
"6.4": [("Đếm mẫu khi các phép xoay được coi là như nhau", "hình tròn chia 6 phần; mẫu xoay trùng nhau chỉ tính một lần", "Liệt kê theo số phần được tô. Với mỗi số, gom các mẫu thu được từ nhau bằng phép quay thành một lớp; chú ý các mẫu có đối xứng quay.", ["2005-T3"])],
"7.1": [("Câu đố “vẫn chưa đủ dữ kiện”", "tích các tuổi là 72, tổng bằng số nhà mà vẫn chưa biết", "Liệt kê mọi bộ thỏa điều kiện đầu. Câu “vẫn chưa biết” cho thấy đáp án nằm trong nhóm có cùng giá trị (ví dụ cùng tổng); dùng gợi ý cuối để chọn.", ["2005-T8", "2013-T10"])],
"7.2": [("Tìm vị trí thắng và thua", "ai đưa quân về góc hoặc lấy viên cuối cùng thì thắng", "Đi lùi từ vị trí kết thúc, đánh dấu vị trí thắng và thua. Tìm chiến lược đối xứng hoặc giữ một bất biến.", ["2024-T9", "2025-T6"])],
"7.3": [("Câu đố lưới logic", "mỗi hàng và mỗi cột có đủ các số; số tòa nhà nhìn thấy; vùng có tổng hoặc tích cho trước", "Bắt đầu từ ô bị ràng buộc nhiều nhất. Mỗi hàng và mỗi cột chứa đủ các số, nên loại trừ dần. Ghi các khả năng còn lại của từng ô.", ["2018-T9", "2016-T9", "2022-T2", "2019-T7", "2015-T1", "2008-T5"])],
"7.4": [("Phủ hoặc chặn với số quân ít nhất", "đặt ít mìn nhất; dùng ít màu nhất để mọi ô L có màu khác nhau", "Chặn dưới bằng đếm: mỗi quân chặn được nhiều nhất k vị trí. Sau đó dựng một ví dụ đạt đúng chặn đó.", ["2010-T8", "2024-T10", "2025-T8", "2008-T8", "2017-T5", "2015-T2"])],
}
for _k, _ids in TEAM_EXAMPLES.items():
    _sub, _i = _k.rsplit("-", 1)
    L[_sub][ord(_i) - 97][3].extend(_ids)
for _sub, _leaves in NEW_LEAVES.items():
    L[_sub].extend(_leaves)
