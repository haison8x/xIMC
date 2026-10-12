# Technique leaves for the KS3 mind map: sub-group -> [(title, sign, key, [example problem ids])]
GROUP_VN = {
 1: ("Lý thuyết số", ""), 2: ("Chữ số & câu đố số", ""), 3: ("Đại số", ""),
 4: ("Số học & bài toán lời văn", ""), 5: ("Hình học", ""), 6: ("Tổ hợp & xác suất", ""),
 7: ("Logic, trò chơi & tối ưu", ""), 8: ("Dãy số & quá trình", ""),
}
SUB_VN = {
 "1.1": "Chia hết, số dư, giai thừa", "1.2": "Số nguyên tố & số ước", "1.3": "Chính phương & lũy thừa", "1.4": "Phương trình nghiệm nguyên, ƯCLN/BCNN",
 "2.1": "Quan hệ chữ số & mật mã", "2.2": "Đếm & cộng chữ số",
 "3.1": "Hệ phương trình & biểu thức đối xứng", "3.2": "Bất đẳng thức & cực trị", "3.3": "Đa thức & định lý Vieta", "3.4": "Phần nguyên & phương trình hàm", "3.5": "Tính toán & rút gọn",
 "4.1": "Tỉ lệ & phần trăm", "4.2": "Trung bình cộng", "4.3": "Chuyển động & đồng hồ", "4.4": "Bài toán lời văn",
 "5.1": "Diện tích & tỉ số diện tích", "5.2": "Săn góc & tam giác", "5.3": "Đường tròn & tiếp xúc", "5.4": "Độ dài, đa giác & Pythagore", "5.5": "Hình khối & gấp giấy", "5.6": "Chứng minh hình học",
 "6.1": "Hoán vị & tổ hợp", "6.2": "Đếm số & xâu có điều kiện", "6.3": "Lưới: đường đi, lát, tô màu", "6.4": "Xác suất", "6.5": "Đồ thị & giải đấu",
 "7.1": "Logic & câu đố hiểu biết", "7.2": "Trò chơi & chiến lược thắng", "7.3": "Cực trị, dựng hình, bất biến", "7.4": "Điền số vào sơ đồ",
 "8.1": "Dãy số & chỉ số", "8.2": "Truy hồi & quá trình lặp", "8.3": "Quy luật trên lưới",
}
L = {
"1.1": [
 ("Dấu hiệu chia hết cho 9, 11 và 99", "số dài chia cho 9; số A36…44B chia hết cho 99", "Một số có cùng số dư khi chia 9 với tổng các chữ số của nó. Chia hết cho 11 khi hiệu (tổng chữ số vị trí lẻ − tổng chữ số vị trí chẵn) chia hết cho 11. 99 = 9 × 11.", ["1999-A1", "2002-A7"]),
 ("Số mũ của p trong n! (công thức Legendre)", "số chữ số 0 ở cuối của n!; C(2021, 1010) chia hết cho 2^M", "Số mũ của p trong n! bằng ⌊n/p⌋ + ⌊n/p²⌋ + … . Số chữ số 0 ở cuối bằng số mũ của 5.", ["2018-A6", "2025-A9", "2021-B3"]),
 ("Số mũ của 2 trong aⁿ − 1", "3^1024 − 1 chia hết cho 2ⁿ, n lớn nhất", "Phân tích a^(2^k) − 1 = (a − 1)(a + 1)(a² + 1)(a⁴ + 1)… Với a lẻ, mỗi thừa số a^(2^i) + 1 (i ≥ 1) chứa đúng một thừa số 2.", ["2007-A7"]),
 ("Chia hết với biểu thức chứa biến", "a + 2 là ước của 3a² + …; n + 1 là ước của …", "n − k là ước của P(n) khi và chỉ khi n − k là ước của P(k). Thay giá trị làm số chia bằng 0 để tìm số dư cố định.", ["2008-A2", "2016-B3", "2021-A10"]),
 ("Biến đổi để mọi điều kiện cùng là “chia hết”", "bốn số liên tiếp lần lượt là bội của 5, 7, 9, 11", "Tìm một biểu thức tuyến tính chia hết cho tất cả các số chia cùng lúc. Ví dụ, 2n − 5 chia hết cho 5, 7, 9 và 11.", ["2001-A4", "2000-A3"]),
 ("Lũy thừa lấy số dư", "chữ số tận cùng của lũy thừa; N chia 2024 dư bao nhiêu", "Số dư của aⁿ lặp lại theo chu kỳ. Định lý Fermat nhỏ: a^(p−1) chia p dư 1 khi p không chia hết a.", ["2000-A1", "2024-A1", "2025-A11"]),
 ("Ước của tổng và tích", "a + b = 2034 và tích ab chia hết cho 2034; ab là ước của baba", "Nếu N = a + b và N chia hết ab thì mỗi ước nguyên tố của N chia hết cả a và b. Lưu ý baba = ba × 101.", ["2012-A1", "2025-A5"]),
],
"1.2": [
 ("Số ước và số ước chính phương", "đúng 14 ước; 55n có đúng 55 ước", "n = p^a · q^b · … có (a + 1)(b + 1)… ước. Số ước chính phương là ∏(⌊aᵢ/2⌋ + 1).", ["2010-A5", "2019-A2", "2022-A2", "2012-A6", "2011-A5"]),
 ("Phương trình với số nguyên tố", "p + q = 192; p, q nguyên tố thỏa …", "Xét chẵn lẻ (có số nào bằng 2 không) và số dư khi chia 3. Đưa về dạng tích để buộc một thừa số bằng 1.", ["2000-A6", "2010-A8", "2021-A8", "2015-A10"]),
 ("Biểu thức là tích của nhiều số nguyên tố", "n² − n + … là tích bốn số nguyên tố", "Chứng minh biểu thức không bao giờ chia hết cho các số nguyên tố nhỏ, rồi chỉ thử với các thừa số lớn hơn.", ["2008-A11"]),
 ("Chứng minh dùng số dư khi chia 7", "không có số nguyên tố tuyệt đối nào chứa đủ 1, 3, 7, 9", "Các hoán vị của 1379 cho đủ mọi số dư khi chia 7. Ghép thêm phần còn lại thì luôn có một hoán vị chia hết cho 7.", ["2007-B3"]),
],
"1.3": [
 ("Hiệu hai bình phương", "x và x + 99 đều là số chính phương", "b² − a² = (b − a)(b + a). Liệt kê các cặp ước có cùng tính chẵn lẻ.", ["2005-A5", "2018-A4"]),
 ("Tổng hoặc tích các số liên tiếp", "tổng 2008 số liên tiếp là số chính phương; 1! · 2! · … · 2012!", "Tổng k số liên tiếp bằng k nhân số ở giữa. Tích là số chính phương khi mọi số mũ trong phân tích đều chẵn.", ["2007-A5", "2011-A3", "2024-A3"]),
 ("Ước lượng số lớn", "một số 53 chữ số bằng nⁿ", "Số chữ số cho biết khoảng chứa n. Chữ số tận cùng giúp xác định chữ số cuối của n.", ["2023-A4", "2000-A5"]),
 ("Xét số dư khi chia 4 và 8", "tổng hai bình phương; kẹp giữa hai số chính phương", "Số chính phương chia 4 dư 0 hoặc 1, chia 8 dư 0, 1 hoặc 4. Số có dạng 4k + 3 không là tổng hai bình phương. Nếu k² < N < (k + 1)² thì N không chính phương.", ["2013-A6", "2008-B3", "2015-B1", "2008-A7", "2017-B1"]),
],
"1.4": [
 ("Đưa về dạng tích", "xy + ax + by = c; m² − n² = …", "Viết xy + ax + by = c thành (x + b)(y + a) = c + ab, rồi liệt kê các cặp ước.", ["2015-A6", "2019-A8", "2019-B2", "2018-A2", "2016-A2"]),
 ("Phương trình 1/x + 1/y = 1/n", "nghiệm nguyên dương của 1/x + 1/y = …", "Biến đổi thành (x − n)(y − n) = n². Số nghiệm bằng số ước của n².", ["2019-A7", "2025-A8"]),
 ("Đặt theo ƯCLN: a = dx, b = dy", "a + b + ƯCLN = BCNN…", "Viết a = d·x, b = d·y với ƯCLN(x, y) = 1. Khi đó BCNN(a, b) = d·x·y.", ["2026-A5", "2013-A9", "2013-A4"]),
 ("Bộ ba chia hết vòng quanh", "a chia hết b + c, b chia hết c + a, c chia hết a + b", "Khi đó a + b + c chia hết cho từng số. Nghiệm có dạng (k, k, k), (k, k, 2k) hoặc (k, 2k, 3k).", ["2025-A1", "2017-A12"]),
 ("Phương trình bậc nhất nghiệm nguyên (bài toán đồng xu)", "số kẹo lớn nhất không mua được bằng túi 6, 9, 20", "Với ax + by = c: tìm một nghiệm, các nghiệm khác hơn kém nhau (b, −a). Với a, b nguyên tố cùng nhau, số lớn nhất không biểu diễn được là ab − a − b.", ["2010-B2", "2021-B2", "2016-A4", "2006-A4", "1999-A8"]),
 ("Sắp thứ tự để chặn biến", "x ≤ y ≤ z; tam giác vuông có cạnh 2009", "Giả sử x ≤ y ≤ z để chặn biến nhỏ nhất, rồi thử hữu hạn trường hợp. Tam giác vuông có cạnh góc vuông a: (c − b)(c + b) = a².", ["2025-A3", "2022-A5", "2023-A5", "2009-A9", "2001-A7"]),
],
"2.1": [
 ("Viết số theo các chữ số", "số có bốn chữ số cộng với các chữ số của nó bằng 2005", "abcd = 1000a + 100b + 10c + d. Đưa về phương trình rồi dùng số dư khi chia 9 hoặc 11 để thu hẹp.", ["2005-A1", "2005-A11", "2002-B1", "2014-A1", "2013-A11"]),
 ("Số vòng 142857", "nhân với 2, 3, 4, 5, 6 vẫn là hoán vị các chữ số", "Đó là chu kỳ của 1/7: 142857.", ["1999-B3"]),
 ("Mật mã chữ cái và điều kiện số học", "ABBCDC là số chính phương; A, B, C có 6 hoán vị…", "Dùng chữ số đầu và cuối để giới hạn, kết hợp số dư khi chia 9, rồi thử hữu hạn trường hợp.", ["2013-A1", "2007-A10", "2024-A7", "2026-A9", "2026-A7"]),
 ("Hiệu sau khi hoán vị chữ số", "a − b chỉ gồm chữ số 1", "Hai số có cùng các chữ số thì hiệu chia hết cho 9. Vì vậy số 11…1 phải có số chữ số 1 là bội của 9.", ["2015-A2", "2015-A8"]),
 ("Tổng chữ số và số lần nhớ", "tổng chữ số của n và n + 1 cùng chia hết cho 26", "S(a + b) = S(a) + S(b) − 9 × (số lần nhớ). Khi n tận cùng bằng k chữ số 9, S(n + 1) = S(n) + 1 − 9k.", ["2009-A10", "2000-B3"]),
],
"2.2": [
 ("Đếm số lần một chữ số xuất hiện", "có bao nhiêu chữ số 0; f(n) = số chữ số 2 từ 1 đến n", "Đếm theo từng hàng. Trong mỗi khối 100 số liên tiếp, mỗi chữ số xuất hiện 10 lần ở hàng chục và 10 lần ở hàng đơn vị.", ["1999-A3", "2014-A11", "2022-A6"]),
 ("Tổng chữ số của tích đặc biệt", "666…6 × 999…9", "x × (10ⁿ − 1) = x·10ⁿ − x. Nếu x có không quá n chữ số thì tích này có tổng chữ số bằng 9n.", ["2016-A6", "2019-A1", "2007-A12"]),
],
"3.1": [
 ("Hệ đối xứng: cộng và trừ các phương trình", "a + bc = b + ca = c + ab", "Cộng tất cả các phương trình để được tổng. Trừ từng cặp, thường được dạng (a − b)(…) = 0.", ["2005-A3", "2005-B1", "2002-B2", "2016-B1", "2018-A12"]),
 ("Hằng đẳng thức", "a + b + c và a² + b² + c² cho trước", "(a + b + c)² = a² + b² + c² + 2(ab + bc + ca). a³ + b³ + c³ − 3abc = (a + b + c)(a² + b² + c² − ab − bc − ca).", ["2004-A2", "2008-A3", "2010-A1", "2021-A12", "2023-A6"]),
 ("Đặt ẩn phụ", "x/a = y/b = z/c; biểu thức đối xứng theo x, y", "Đặt x/a = y/b = z/c = k thì x = ak, y = bk, z = ck. Với biểu thức đối xứng hai biến, đặt S = x + y và P = xy.", ["2006-A6", "2002-A10", "2017-A11", "2014-A7", "2024-A2"]),
 ("Tổng bình phương bằng 0", "phương trình chứa căn; (2x + 1)² + … = 0", "Các số hạng không âm có tổng bằng 0 thì từng số hạng bằng 0. Với căn thức, đặt t bằng biểu thức dưới căn.", ["2006-A9", "2001-A8", "2021-A6", "2026-A4"]),
],
"3.2": [
 ("Bất đẳng thức AM–GM", "giá trị nhỏ nhất của phân thức với các số dương", "a + b ≥ 2√(ab), dấu bằng khi a = b. Tách các số hạng sao cho tích của chúng là hằng số.", ["2001-B1", "2017-A5", "2022-A3", "2008-A4"]),
 ("Thêm bớt để thành bình phương", "giá trị nhỏ nhất của biểu thức bậc hai", "ax² + bx + c = a(x + b/(2a))² + … Với hai biến, nhóm theo từng biến rồi thêm bớt.", ["2004-A12", "2023-A1", "2026-A10", "2017-A7"]),
 ("Cực trị khi có ràng buộc tuyến tính", "−4 ≤ f(1) ≤ −1 và −1 ≤ f(2) ≤ 5, tìm f(8) lớn nhất", "Viết đại lượng cần tìm thành tổ hợp của các đại lượng đã biết khoảng giá trị: f(8) = α·f(2) + β·f(1). Dồn tổng vào càng ít biến càng tốt.", ["2008-A9", "2017-A9", "2017-A4", "2014-A4"]),
 ("Kẹp giữa hai số nguyên", "phần nguyên của k; n lớn nhất thỏa bất đẳng thức", "Chặn biểu thức giữa hai số nguyên liên tiếp để lấy phần nguyên hoặc tìm n lớn nhất.", ["2012-B2", "2006-A12", "2011-A12", "2025-A12"]),
],
"3.3": [
 ("Định lý Vieta", "α, β là hai nghiệm; tính α − β, (a − c)(a − d)…", "x₁ + x₂ = −b/a, x₁·x₂ = c/a. Biến đổi biểu thức cần tính về tổng và tích của hai nghiệm.", ["2005-A7", "2022-A1", "2022-A7", "2024-A5", "2011-B2"]),
 ("Đa thức nhận các giá trị cho trước", "P(1) = 10, P(2) = 20, P(3) = 30", "P(x) − 10x có các nghiệm 1, 2, 3, nên P(x) = (x − 1)(x − 2)(x − 3)(x − r) + 10x.", ["2002-A4", "2018-A7", "2010-A6"]),
 ("Hai tam thức có cùng hệ số cao nhất", "f, g bậc hai, hệ số đầu bằng 1", "f − g là đa thức bậc nhất, nên f(x) = g(x) có đúng một nghiệm.", ["2017-B3", "2021-A3"]),
 ("Điều kiện có nghiệm", "đặt t = 3ˣ; ba nghiệm là ba cạnh tam giác vuông", "Đặt ẩn phụ rồi yêu cầu Δ > 0 và điều kiện về tổng, tích. Nếu các nghiệm là cạnh tam giác vuông thì kết hợp Vieta với Pythagore.", ["2001-B2", "2018-B1", "2026-A3"]),
],
"3.4": [
 ("Phần nguyên và phần lẻ", "25{x} + [x] = 125", "x = [x] + {x} với 0 ≤ {x} < 1. Đặt n = [x], giải theo n rồi kiểm tra điều kiện của {x}.", ["2007-A11", "2004-A11", "2023-B1", "2024-A10", "2008-B1"]),
 ("Phương trình hàm", "f(a)³ + f(b)³ + f(c)³ = 3f(a)f(b)f(c)", "Thay các giá trị đặc biệt (a = b = c, 0, 1) để tìm f.", ["2019-A10"]),
],
"3.5": [
 ("Tổng rút gọn (telescoping)", "tích hoặc tổng phân số có dạng lặp", "Tách 1/(k(k + 1)) = 1/k − 1/(k + 1). Với tích, các tử và mẫu sẽ triệt tiêu chéo nhau.", ["2009-A6", "2001-A9", "1999-A5", "2005-A10"]),
 ("Đặt số lớn làm ẩn", "1234567891 × 1234567896 × …", "Đặt n bằng số lớn (ví dụ n = 1234567890) rồi khai triển như một đa thức theo n.", ["2014-A2", "2012-B1", "2013-B1"]),
 ("Chứng minh tổng bằng 1", "tổng các phân số 1/(pq) bằng 1", "Quy nạp theo n: khi n tăng thêm 1, phần bị mất và phần được thêm vào có tổng bằng nhau.", ["2025-B1", "2000-A2"]),
],
"4.1": [
 ("Đưa về cùng một lượng", "2/5 tiểu thuyết và 3/4 sách giáo khoa có bìa cứng", "Đặt lượng chung bằng x rồi quy mọi phân số về theo x.", ["2017-A1", "2002-A1"]),
],
"4.2": [
 ("Trung bình nhóm: độ lệch triệt tiêu", "trung bình nhóm đậu và nhóm trượt; chuyển một người sang làng khác", "Σ nᵢ(mᵢ − m) = 0. Khi một người chuyển nhóm, xem tổng của mỗi nhóm thay đổi như thế nào.", ["2009-A8", "2017-A2", "2016-A10", "2007-A1"]),
],
"4.3": [
 ("Kim đồng hồ và đường có dốc", "nhầm kim giờ với kim phút; lên dốc 56, xuống dốc 72 km/h", "Kim phút quay 6°/phút, kim giờ 0,5°/phút. Ở lượt về, đoạn lên dốc thành xuống dốc và ngược lại.", ["2001-A5", "2006-A7"]),
 ("Bài toán trung chuyển", "xe tải quay lại đón khoai từ xe bò", "Vẽ sơ đồ thời gian – quãng đường. Các xe đến cùng lúc nên thời gian bằng nhau.", ["2015-A5"]),
],
"4.4": [
 ("Hệ phương trình tuyến tính từ lời văn", "A + B ít hơn C 6 quả…; thang nhiệt độ", "Đặt ẩn, mỗi câu trong đề cho một phương trình. Hai thang đo tuyến tính thì ứng với nhau qua một hàm bậc nhất.", ["2009-A3", "2010-A2", "1999-A12", "2000-A10", "2006-A1"]),
 ("Dùng điều kiện nghiệm nguyên", "số chai bán được, số đồng xu, đội hình hình chữ nhật", "Sau khi lập phương trình, dùng điều kiện nghiệm là số nguyên dương để chốt đáp án.", ["2009-A12", "2016-A7", "2007-A4", "2010-A11", "2016-A1"]),
],
"5.1": [
 ("Tỉ số diện tích bằng tỉ số đáy (đường nối từ đỉnh)", "BE và CF cắt nhau tại D; các tam giác có diện tích bằng nhau", "Hai tam giác chung chiều cao thì tỉ số diện tích bằng tỉ số đáy. Đặt ẩn cho các phần chưa biết rồi lập hệ.", ["2007-A3", "2016-A5", "2017-A8", "2004-A3", "1999-A10", "2024-A6"]),
 ("Hình bình hành và trung điểm", "E, F là trung điểm; BD cắt AE tại M", "Trọng tâm chia trung tuyến theo tỉ số 2 : 1. Tam giác có đáy là một cạnh và đỉnh nằm trên cạnh đối diện bằng ½ hình bình hành.", ["2006-A5", "2014-A8", "2015-A11", "2019-A6", "2002-A6", "2006-A8"]),
 ("Tứ giác có hai đường chéo cắt nhau", "S(AOB) = 144, S(COD) = 169, tìm diện tích ABCD nhỏ nhất", "S(AOB) · S(COD) = S(BOC) · S(AOD). Theo AM–GM, tổng nhỏ nhất khi hai tam giác còn lại có diện tích bằng nhau.", ["2026-A1", "2005-B2"]),
 ("Khoảng cách tỉ lệ với diện tích", "khoảng cách từ E, D, C tới AB lần lượt là 7, 5, 11", "Hai tam giác chung đáy thì tỉ số diện tích bằng tỉ số khoảng cách tới đáy. Một điểm chia đoạn thẳng theo tỉ lệ thì khoảng cách của nó là trung bình có trọng số.", ["2026-A12", "2013-A2", "2023-A3", "2023-A8"]),
],
"5.2": [
 ("Săn góc với tam giác cân", "điểm P trong tam giác, cho trước các góc", "Đánh dấu các cạnh bằng nhau để suy ra góc bằng nhau. Khi thấy góc 60° hoặc 30°, thử dựng thêm tam giác đều.", ["2017-A10", "2022-A12", "2024-A4", "2021-A9", "2009-B2", "2010-A10"]),
 ("Đường phân giác", "BD là phân giác của góc ABC", "Đường phân giác chia cạnh đối diện theo tỉ lệ hai cạnh kề: BD/DC = AB/AC. Đường phân giác ngoài cũng có tính chất tương tự.", ["2002-A9", "2006-A3", "2012-B3", "2018-B3"]),
 ("Góc nội tiếp và đa giác đều", "∠P₁P₇P₈ = …; hình thoi có góc cho trước", "Góc nội tiếp bằng ½ cung bị chắn. Các đỉnh của n-giác đều chia đường tròn thành n cung, mỗi cung 360°/n.", ["2025-A2", "2026-A6", "2002-A11", "2009-A4"]),
],
"5.3": [
 ("Đường tròn nội tiếp", "đường tròn tiếp xúc cả bốn cạnh; r = 4 và các đoạn tiếp tuyến là số liên tiếp", "Hai tiếp tuyến kẻ từ một điểm bằng nhau. r = S/p (S là diện tích, p là nửa chu vi). Tứ giác ngoại tiếp: AB + CD = AD + BC.", ["2001-A6", "2016-A3", "2010-B1", "2005-A6", "1999-A7"]),
 ("Các đường tròn tiếp xúc nhau", "các đường tròn tiếp xúc nhau và tiếp xúc cạnh hình vuông", "Khoảng cách hai tâm bằng tổng bán kính (tiếp xúc ngoài) hoặc hiệu bán kính (tiếp xúc trong). Nối các tâm để có tam giác vuông.", ["2011-A7", "2013-A5", "2013-A10", "2010-A7", "2012-A2", "2025-A4", "2012-A11"]),
 ("Tứ giác nội tiếp và định lý Ptolemy", "A, B, C, D nằm trên đường tròn; tính độ dài BC", "Tứ giác nội tiếp có hai góc đối bù nhau. Ptolemy: AC·BD = AB·CD + AD·BC. Hai dây cắt nhau: AE·EB = CE·ED.", ["2014-A12", "2022-A4", "2017-A6", "2012-A8", "2025-B2", "2004-A1"]),
 ("Cung tròn và dãy đường tròn", "các cung giữa đỉnh tam giác và đỉnh thất giác; dãy đường tròn vô hạn", "Độ dài cung tỉ lệ với góc ở tâm. Dãy đường tròn đồng dạng cho tổng là cấp số nhân.", ["2018-A10", "2023-A2", "2006-A2", "2018-A5"]),
],
"5.4": [
 ("Đặt tọa độ và Pythagore", "PA = 4, PB = 6, PD = 9, tìm PC", "Đặt hệ trục tọa độ cho hình vuông hoặc hình chữ nhật. Với P bất kỳ trong hình chữ nhật: PA² + PC² = PB² + PD².", ["2000-A9", "1999-B2", "2021-A5", "2019-B3", "2025-A6"]),
 ("Gấp giấy", "gấp theo AE để B rơi xuống CD", "Nếp gấp là trung trực của đoạn nối điểm cũ và điểm mới. Các đoạn chồng lên nhau bằng nhau, rồi dùng Pythagore.", ["2010-A4"]),
 ("Tam giác đồng dạng", "bóng của cột; DE song song AB", "Hai góc bằng nhau thì hai tam giác đồng dạng, các cạnh tương ứng tỉ lệ. Bài về bóng nắng là bài đồng dạng.", ["1999-A4", "2016-A8", "2014-A5", "2022-A9", "2005-A2"]),
 ("Diện tích hoặc độ dài lớn nhất, nhỏ nhất", "bốn hàng rào dài 1, 4, 7, 8; BQ nhỏ nhất", "Tứ giác có các cạnh cho trước đạt diện tích lớn nhất khi nội tiếp được (công thức Brahmagupta). Với độ dài nhỏ nhất, tìm quỹ tích điểm di động.", ["2007-A8", "2022-B2", "2024-B2"]),
],
"5.5": [
 ("Cắt góc đa diện và gấp tam giác", "cắt một hình chóp ở mỗi đỉnh của đa diện 36 cạnh", "Cắt một đỉnh bậc d tạo thêm d cạnh. Tổng bậc các đỉnh bằng 2 lần số cạnh. Khi gấp, phần gấp đối xứng qua nếp gấp.", ["2006-A11", "2007-A6"]),
],
"5.6": [
 ("Chứng minh bốn điểm cùng nằm trên một đường tròn", "chứng minh P, Q, R, S cùng thuộc một đường tròn; OP ⊥ BC", "Chứng minh hai góc cùng nhìn một đoạn thẳng bằng nhau, hoặc tích hai đoạn bằng nhau (phương tích).", ["2026-B3", "2023-B3", "2009-A7"]),
 ("Chứng minh đẳng thức về đoạn thẳng", "A'E + FG = A'G; BE = CF = ½(AB + AC)", "Dựng tam giác bằng nhau, kẻ đường phụ qua trung điểm hoặc song song với đường phân giác.", ["2000-B1", "2002-B3", "2004-B3", "2001-B3", "2011-B1"]),
],
"6.1": [
 ("Hoán vị có điều kiện", "không chứa YOU và ME; xếp quanh bàn tròn", "Dùng bao hàm – loại trừ cho các khối bị cấm. Xếp n người quanh bàn tròn có (n − 1)! cách.", ["2013-A3", "2018-A9", "2014-A9", "2026-A11"]),
 ("Chia vật giống nhau và chọn tập rời nhau", "chia 31 tấm thảm; hai gói hàng không có món chung", "Chia n vật giống nhau cho k phần: C(n + k − 1, k − 1). Số cặp tập con khác rỗng, rời nhau, không xét thứ tự của n phần tử: (3ⁿ − 2·2ⁿ + 1)/2.", ["2026-A2", "2013-A8", "2026-A8"]),
 ("Thứ tự từ điển", "biển số xe thứ 7000", "Cố định các chữ số đầu, đếm số hoán vị của phần còn lại, rồi trừ dần.", ["2004-A4"]),
 ("Đếm hình tạo bởi điểm trên đường tròn hoặc lưới", "đa giác lồi từ 2009 điểm; nối 14 điểm bằng 7 dây cung không cắt nhau", "Đa giác lồi ứng với một tập con có từ 3 điểm trở lên. Số cách nối 2n điểm bằng n dây không cắt nhau là số Catalan; với n = 7, C₇ = 429.", ["2009-A11", "2012-A10", "2022-A8", "2024-A8", "2012-A12"]),
],
"6.2": [
 ("Đếm số theo ràng buộc chữ số", "chỉ dùng chữ số 0, 1, 2; tích các chữ số là 120 và tổng là 20", "Chọn từng chữ số theo ràng buộc. Nếu số bị chặn trên (≤ 20112012) thì đếm theo tiền tố.", ["1999-A6", "2012-A7", "2012-A9", "2022-A11", "2019-A5"]),
 ("Truy hồi cho xâu ký tự", "các chữ số 3 không đứng cạnh nhau; dãy OE", "Phân loại theo ký tự cuối cùng để lập công thức truy hồi. Thường ra dãy Fibonacci.", ["2008-A5", "2004-B1", "2011-A10"]),
],
"6.3": [
 ("Đường đi trên lưới", "chỉ đi lên hoặc sang phải, tránh các điểm hỏng", "Không có chướng ngại vật thì có C(m + n, m) đường. Có điểm cấm thì điền số cách đi tới từng nút, hoặc trừ đi số đường đi qua điểm cấm.", ["2008-A1", "2019-A9", "2023-A12"]),
 ("Tô màu và lát gạch", "ô 2×6 với 3 màu; tô màu các đỉnh lục giác; lát domino", "Lập truy hồi theo từng cột. Tô k màu cho n đỉnh của một vòng sao cho hai đỉnh kề khác màu: (k − 1)ⁿ + (−1)ⁿ(k − 1) cách.", ["2012-A5", "2023-B2", "2018-B2", "2026-B1", "2015-A9", "2013-A12", "2004-A6"]),
 ("Đếm hình chữ nhật", "hình chữ nhật có diện tích 12; hình chữ nhật tránh hố đen", "Đếm theo kích thước: trong lưới m × n ô, hình a × b có (m − a + 1)(n − b + 1) vị trí. Trừ đi các hình chứa ô bị cấm.", ["1999-A11", "2015-A4", "2021-A1"]),
],
"6.4": [
 ("Xác suất cổ điển và xác suất theo từng bước", "tung đồng xu; chọn hộp ngẫu nhiên rồi lấy bi", "Xác suất = số trường hợp thuận lợi / tổng số trường hợp. Quá trình nhiều bước thì nhân xác suất theo từng nhánh rồi cộng các nhánh.", ["2018-A3", "2019-A3", "2015-B2", "2016-A11", "2025-B3"]),
],
"6.5": [
 ("Đồ thị không có tam giác", "trong ba người bất kỳ có hai người chưa đấu với nhau", "Số cạnh lớn nhất là ⌊n²/4⌋, đạt được khi chia thành hai nhóm và chỉ nối giữa hai nhóm.", ["2009-B1"]),
 ("Đường đi và chu trình trên đồ thị", "kiến bò trên khung lập phương; đi qua các cây cầu", "Một đường đi qua mỗi cạnh đúng một lần cần số đỉnh bậc lẻ là 0 hoặc 2. Đếm đường đi dài k bằng truy hồi theo từng bước.", ["1999-B1", "2018-A1", "2021-A11", "2007-B2"]),
],
"7.1": [
 ("Câu đố “tôi không biết”", "Albert và Bill không biết số trên mũ của mình", "Liệt kê mọi khả năng. Mỗi câu “không biết” loại bỏ các trường hợp mà người đó có thể có đáp án duy nhất.", ["2004-A10", "2011-A6"]),
 ("Người nói thật và người nói dối", "câu trả lời “kẻ nói dối” được nói 240 lần", "Mỗi cặp gồm một người nói thật và một người nói dối tạo ra 2 câu “kẻ nói dối”, nên tổng số câu là 2·t·l.", ["2011-A2", "2010-A12"]),
],
"7.2": [
 ("Tìm vị trí thua", "người viết số 1 thắng; ngày 31/12 thắng", "Đi lùi từ đích để tìm các vị trí thua (đến lượt ai ở đó thì người đó thua). Có thể dùng chiến lược ghép cặp hoặc đối xứng.", ["2024-B3", "2025-A7", "2022-B1"]),
],
"7.3": [
 ("Tìm đại lượng bất biến", "thay a, b bằng a + b + ab; lật hai đồng xu kề nhau", "Tìm đại lượng không đổi sau mỗi bước, ví dụ tích các (a + 1), hoặc tính chẵn lẻ.", ["2014-B1", "2024-B1", "2013-B3", "2021-A2"]),
 ("Chặn trên rồi dựng ví dụ", "điểm lớn nhất; số góc tù nhiều nhất", "Dùng lập luận đếm để chặn trên, sau đó dựng một ví dụ đạt đúng chặn đó.", ["2006-B1", "2007-B1", "2011-B3", "2023-A10", "2024-A11", "2025-A10"]),
 ("Sắp xếp để đạt cực trị", "tổng hiệu các tuổi kề nhau lớn nhất", "Xếp xen kẽ số lớn và số nhỏ để tổng các hiệu kề nhau lớn nhất. Với tổng các tập con, so sánh nhóm lớn nhất với nhóm nhỏ nhất.", ["2009-A5", "2021-A4", "2015-A3", "2010-A9"]),
 ("Thuật toán tối ưu", "qua cầu với một đèn lồng; mở két mật mã", "Qua cầu: cho hai người chậm nhất đi cùng nhau. Muốn thử mọi mật mã 3 chữ số, mỗi chữ số có 3 giá trị, cần 3³ + 2 = 29 lần bấm (chuỗi de Bruijn).", ["2007-A2", "2024-A9", "2002-A3", "2023-A11"]),
 ("Chuồng bồ câu và phân hoạch", "chia 1..30 thành các nhóm, không có hai số cộng lại thành số chính phương", "Tìm một tập các phần tử đôi một xung đột để chặn dưới số nhóm, rồi dựng một cách phân hoạch đạt chặn đó.", ["2006-B3", "2023-A9", "2004-A9", "2024-A12"]),
],
"7.4": [
 ("Điền số với tổng bằng nhau", "tổng 4 ô của mọi hình vuông bằng nhau; tổng mỗi vòng tròn là bội của 6", "Cộng tất cả các tổng: các ô chung được đếm nhiều lần. Từ đó suy ra số ở ô trung tâm.", ["2004-A7", "2015-A1"]),
],
"8.1": [
 ("Dãy liên quan đến hệ cơ số", "1, 3, 4, 9, 10, 12, …; số dạng 2^a + 2^b", "Số hạng thứ n của dãy các tổng lũy thừa phân biệt của 3: viết n ở hệ nhị phân rồi đọc như số ở hệ cơ số 3.", ["2019-B1", "2023-A7"]),
 ("Cấp số cộng và dãy tuần hoàn", "tổng ba số kề nhau luôn bằng 20; tháp xếp khối ở góc phòng", "Tổng cấp số cộng = (đầu + cuối) × số số hạng / 2. Tổng ba số kề không đổi thì dãy tuần hoàn chu kỳ 3. Tháp góc dùng tổng các số tam giác: n(n + 1)(n + 2)/6.", ["2000-A4", "2000-A12", "2019-A12"]),
],
"8.2": [
 ("Bài toán Josephus", "loại người theo vòng, tìm người cuối cùng", "Mô phỏng với n nhỏ để tìm quy luật. Với luật bỏ người thứ hai: viết n = 2^m + l thì người còn lại ở vị trí 2l + 1.", ["2002-A8"]),
 ("Lập truy hồi đếm số bước", "tháp chỉ được chuyển sang cọc kề; số mảnh giấy xé", "Đặt a(n) là số bước với n đĩa, lập công thức theo a(n − 1). Tháp chỉ chuyển sang cọc kề cần 3ⁿ − 1 bước.", ["2014-B3", "2010-B3", "2006-A10"]),
 ("Dãy trên vòng tròn và quá trình lặp", "mỗi số bằng hiệu của hai số tiếp theo; máy biến n thành n(n + 1)", "Tìm chu kỳ hoặc dạng tổng quát, và dùng một bất biến của quá trình (tổng, số lớn nhất).", ["2008-A6", "2022-A10", "2005-B3", "2009-A2"]),
],
"8.3": [
 ("Chuỗi ô tô màu trên lưới", "chuỗi ô màu xám trên lưới 101 × 101", "Đếm số ô cho các lưới nhỏ (n = 1, 3, 5, …), tìm quy luật rồi tổng quát lên.", ["2019-A4"]),
],
}


# ---- Team-paper additions --------------------------------------------------
# Leaf ids ("1.1-a") key the saved progress in the page, so new leaves are only ever
# appended at the end of a sub-group; team problems are added as extra examples.
TEAM_EXAMPLES = {
 "1.1-a": ["2022-T1", "2019-T4"], "1.1-f": ["2017-T7", "2025-T6", "2006-T7", "2004-T4"],
 "1.2-a": ["2012-T6", "2014-T6", "2016-T10", "2018-T7", "2018-T1", "2009-T2"], "1.2-b": ["2014-T2", "2019-T1", "2005-T8", "2021-T9"],
 "1.3-a": ["2006-T10", "2021-T4", "2023-T6"], "1.3-b": ["2018-T4", "2008-T10"], "1.3-d": ["2015-T2", "2015-T9", "2025-T3", "2026-T2", "2023-T7"],
 "1.4-a": ["2010-T3", "2017-T4", "2018-T2", "2024-T1"], "1.4-b": ["2002-T4", "1999-T3", "2000-T5", "2005-T10"],
 "1.4-c": ["2000-T3", "2022-T9"], "1.4-d": ["2014-T5"], "1.4-f": ["2005-T1", "2025-T1", "2014-T3", "2009-T10"],
 "2.1-a": ["2001-T5", "2006-T5", "2016-T2", "2012-T5"], "2.1-c": ["2012-T10", "2001-T7"],
 "2.2-a": ["2024-T3"], "2.2-b": ["2019-T10"],
 "3.1-a": ["2010-T1", "2021-T2", "2022-T5", "2002-T1"], "3.1-b": ["2026-T4", "2016-T7"], "3.1-d": ["2011-T1"],
 "3.2-a": ["2017-T8", "2026-T6", "2009-T6"], "3.2-d": ["2010-T5", "2018-T5"],
 "3.3-a": ["2023-T1", "2024-T2", "2025-T2", "2017-T5"], "3.3-b": ["2011-T6"],
 "3.4-a": ["2006-T8", "2025-T4"], "3.4-b": ["2022-T2", "2002-T2"], "3.5-a": ["2014-T1", "2021-T5"],
 "4.2-a": ["2012-T2"],
 "5.1-a": ["2018-T8", "2021-T7"], "5.1-b": ["2018-T3", "2015-T8", "2022-T7", "2025-T5"], "5.1-d": ["2013-T7"],
 "5.2-a": ["2010-T7", "2013-T4", "2014-T9", "2015-T10", "2023-T3", "2024-T7", "2026-T3", "2021-T3", "2011-T8"],
 "5.3-a": ["2006-T1"], "5.3-b": ["2026-T7", "2017-T3"], "5.3-c": ["2008-T7", "2016-T4", "2021-T8", "2022-T4", "2022-T8", "2014-T8"],
 "5.3-d": ["2025-T9"],
 "5.4-a": ["2001-T6", "2015-T3", "2024-T5", "2023-T5", "2013-T2"], "5.4-d": ["2004-T1", "2006-T9", "2019-T3", "2019-T6", "2009-T8"],
 "5.5-a": ["2000-T6", "2017-T1"],
 "5.6-a": ["2017-T6", "2023-T2"], "5.6-b": ["2000-T1", "2002-T6", "2002-T7", "2005-T4", "2024-T4", "2026-T10", "2007-T8", "2010-T2"],
 "6.1-a": ["2022-T6", "2015-T4"], "6.1-b": ["2019-T5", "2026-T1"], "6.1-d": ["2019-T8"],
 "6.2-a": ["2008-T8", "2023-T9", "2025-T10"], "6.2-b": ["2014-T7", "2021-T10", "2026-T8", "2018-T10", "2012-T4"],
 "6.3-a": ["2010-T10"], "6.3-b": ["2007-T10", "2019-T9"], "6.3-c": ["2010-T4", "2011-T4", "2024-T8", "2017-T10"],
 "6.4-a": ["2013-T3"], "6.5-b": ["2009-T4", "2021-T6"],
 "7.1-a": ["2011-T10"],
 "7.2-a": ["2006-T6", "2005-T6", "2013-T8", "2024-T10"],
 "7.3-a": ["2008-T5", "2017-T2", "2026-T5", "2012-T1"],
 "7.3-b": ["2010-T6", "2011-T9", "2016-T5", "2016-T8", "2026-T9", "2023-T8", "2008-T4", "2018-T6"],
 "7.3-c": ["2001-T2", "2007-T9", "2007-T7"], "7.3-d": ["2008-T9", "2023-T4", "2022-T3", "2019-T7", "2025-T7"],
 "7.3-e": ["2005-T2", "2019-T2", "2004-T5", "2015-T5"],
 "7.4-a": ["2001-T1", "2007-T1", "2007-T3", "2010-T9", "2013-T1", "2015-T1", "2016-T1", "2012-T3", "2021-T1"],
 "8.1-a": ["2005-T3", "2022-T10"], "8.2-a": ["2011-T7", "2009-T1", "1999-T2", "2024-T9"], "8.2-c": ["2013-T5"],
}
NEW_LEAVES = {
"1.1": [("Số có bình phương tận cùng bằng chính nó", "bình phương một số có đuôi bằng chính số đó", "x² − x = x(x − 1) chia hết cho 10ᵏ = 2ᵏ · 5ᵏ. Vì x và x − 1 nguyên tố cùng nhau, một số chia hết cho 2ᵏ và số còn lại chia hết cho 5ᵏ.", ["2007-T4"])],
"5.2": [("Cắt tam giác thành tam giác cân", "cắt một tam giác thành hai tam giác cân; kéo dài cạnh để được tam giác cân", "Đường cắt đi qua một đỉnh. Xét lần lượt các khả năng hai cạnh bằng nhau trong mỗi tam giác con, rồi dùng tổng góc 180° để lập phương trình.", ["2006-T2", "2008-T6"])],
"6.3": [("Cắt ghép và lát bằng polyomino", "chia hình thành các mảnh giống nhau; lát bằng pentomino hoặc quân hình chữ V", "Tô màu ô cờ (hoặc tô 3 màu) để chứng minh không lát được. Diện tích phải chia hết cho số mảnh. Bắt đầu từ góc hoặc từ ô bị ràng buộc nhiều nhất.", ["2001-T4", "2005-T9", "2002-T3", "1999-T4", "2004-T7", "2016-T9", "2013-T10"])],
"6.5": [("Mỗi cặp gặp nhau đúng một lần", "mỗi học sinh trực 3 ngày, không cặp nào trực chung quá một lần", "Đếm số cặp theo hai cách: mỗi nhóm k người chứa C(k, 2) cặp, còn tổng số cặp có thể có là C(n, 2). Từ đó chặn số nhóm.", ["2025-T8", "2009-T9"]),
        ("Bảng điểm giải đấu", "thắng, hòa, thua; đổi hệ điểm từ 2 sang 3 điểm", "Tổng điểm của cả giải tính theo số trận thắng và số trận hòa. Lập hệ với số trận của từng đội, rồi dùng điều kiện nghiệm nguyên.", ["2004-T6", "2007-T6", "2013-T6"])],
"7.1": [("Suy luận từ các dự đoán", "mỗi giáo viên đoán đúng một số vị trí", "Lập bảng các dự đoán, thử từng giả thiết về người đoán đúng, rồi loại các trường hợp mâu thuẫn.", ["2000-T4"])],
"7.3": [("Câu đố đường đi và bố trí", "vẽ đường khép kín qua các ô; che ô sao cho không còn số trùng", "Bắt đầu từ các ô bị ép buộc (ô góc, ô chỉ còn hai lối đi). Dùng tô màu chẵn lẻ để loại trường hợp.", ["2008-T3", "2009-T5", "2008-T2", "2007-T2", "2002-T8", "2014-T10"])],
"7.4": [("Ô vuông Latin và câu đố tòa nhà", "mỗi hàng, cột và đường chéo có đủ 1 … n; số tòa nhà nhìn thấy", "Mỗi số xuất hiện đúng một lần trên mỗi hàng và mỗi cột. Bắt đầu từ các đường chéo và các gợi ý ở biên, rồi loại trừ dần.", ["1999-T5", "2009-T3", "2004-T3", "2006-T4", "2023-T10"])],
}
for _k, _ids in TEAM_EXAMPLES.items():
    _sub, _i = _k.rsplit("-", 1)
    L[_sub][ord(_i) - 97][3].extend(_ids)
for _sub, _leaves in NEW_LEAVES.items():
    L[_sub].extend(_leaves)
