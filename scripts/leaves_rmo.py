# Technique leaves for the RMO mind map: sub-group -> [(title, sign, key, [example problem ids])].
# Few, broad leaves on purpose, so that every leaf collects several problems.
GROUP_VN = {
 1: ("Số học", "Number Theory"),
 2: ("Tính toán khéo", "Clever Calculation"),
 3: ("Chữ số & quy luật", "Digits & Patterns"),
 4: ("Toán có lời văn", "Word Problems"),
 5: ("Hình học", "Geometry"),
 6: ("Tổ hợp & logic", "Combinatorics & Logic"),
}
SUB_VN = {
 "1.1": "Chia hết, số dư, chữ số tận cùng & chu kỳ", "1.2": "Ước, số nguyên tố, ƯCLN/BCNN & phương trình nghiệm nguyên",
 "2.1": "Tổng dãy: khử liên tiếp & cấp số nhân", "2.2": "Đặt ẩn phụ, nhóm số hạng & rút thừa số chung",
 "3.1": "Chữ số: tổng chữ số, đếm chữ số, cấu tạo số", "3.2": "Bảng số, dãy số & quá trình lặp",
 "4.1": "Tỉ số, phần trăm, pha trộn & lập phương trình", "4.2": "Chuyển động, đồng hồ & năng suất",
 "5.1": "Diện tích & tỉ số diện tích đa giác", "5.2": "Hình tròn, cung & phần tô màu", "5.3": "Góc, độ dài & hình khối",
 "6.1": "Đếm cách sắp xếp & chọn", "6.2": "Đếm hình, đường đi & truy hồi", "6.3": "Logic, Dirichlet, trò chơi & cực trị",
}
L = {
"1.1": [
 ("Chia hết cho số ghép (33, 55, 88, 99, 198, 999)", "số dài có chữ số ẩn hoặc lặp khối, hỏi chia hết hay số dư cho một số ghép", "tách số chia thành tích các số nguyên tố cùng nhau (99 = 9 × 11, 88 = 8 × 11, 198 = 2 × 9 × 11) rồi dùng dấu hiệu chia hết cho từng thừa số; chia cho 99 / 999 thì cộng các nhóm 2 / 3 chữ số từ phải sang", ["2014-9", "2015-13", "2022-3", "2025-12", "2011-14", "2023-4", "2018-13", "2013-17"]),
 ("Chia hết cho 7, 13: khối 1001 và 111111", "số gồm nhiều chữ số lặp lại (55…5X99…9, 666666XY444444), hỏi chia hết cho 7 hoặc 13", "1001 = 7 × 11 × 13 nên 111111 chia hết cho 7 và 13: bỏ đi từng khối 6 chữ số giống nhau, chỉ xét phần còn lại", ["2012-13", "2018-15"]),
 ("Chữ số tận cùng của lũy thừa và tổng đan dấu", "hỏi chữ số tận cùng (hoặc 2 chữ số tận cùng) của lũy thừa lớn hay tổng lập phương đan dấu", "chữ số tận cùng của lũy thừa lặp theo chu kỳ 4; ghép cặp các số hạng liền nhau; 2 chữ số tận cùng thì xét số dư khi chia cho 4 và 25", ["2010-9", "2014-7", "2021-12", "2021-17", "2016-15", "2018-12", "2017-17", "2018-17"]),
 ("Chu kỳ số dư: lũy thừa, giai thừa, ngày trong tuần, chữ số thập phân", "số dư của lũy thừa, tổng giai thừa, dãy Fibonacci; thứ trong tuần sau n ngày; chữ số thứ n sau dấu phẩy", "tìm chu kỳ của số dư rồi lấy n chia cho độ dài chu kỳ; từ k! chia hết cho số chia thì các số hạng sau bằng 0; nhiều điều kiện số dư thì tìm số nhỏ nhất rồi cộng BCNN", ["2008-12", "2009-16", "2013-20", "2016-7", "2021-16", "2017-10", "2024-1", "2014-15", "2013-4", "2008-3", "2008-6", "2016-13", "2022-2", "2022-12"]),
],
"1.2": [
 ("Số ước qua phân tích thừa số nguyên tố", "hỏi số ước, số ước chính phương, số cặp (m, n) có tích cho trước; bật/tắt tủ khóa theo ước", "n = p^a × q^b × … có (a + 1)(b + 1)… ước; ước chính phương thì chọn số mũ chẵn; vật bị bật tắt bằng số ước của nó, chỉ số chính phương có số ước lẻ", ["2010-3", "2015-3", "2016-4", "2021-3", "2011-1", "2025-4", "2008-13", "2015-7", "2022-19"]),
 ("ƯCLN, BCNN và cùng số dư", "bộ số có ƯCLN/BCNN cho trước, cắt hình vuông lớn nhất, các số chia cho A cùng số dư, đếm vòng tròn", "phân tích ra thừa số nguyên tố và so số mũ từng thừa số; cùng số dư khi chia cho A thì A là ước của các hiệu; tổng số câu là bội của BCNN các mẫu", ["2008-19", "2010-18", "2012-5", "2017-19", "2021-20", "2024-12", "2011-7", "2010-8"]),
 ("Phương trình nghiệm nguyên, số nguyên tố, tổng số liên tiếp", "tìm số nghiệm nguyên dương của 1/m − 1/n = …, a² − b² = …; biểu diễn thành tổng các số liên tiếp; điều kiện số nguyên tố", "biến đổi về dạng tích = hằng số rồi đếm cặp ước; tổng k số liên tiếp = k × số ở giữa; 2 là số nguyên tố chẵn duy nhất, xét chẵn lẻ", ["2011-17", "2014-4", "2014-10", "2018-20", "2024-5", "2024-6", "2014-19", "2023-10", "2023-9", "2025-16"]),
 ("Đếm bội: bao hàm – loại trừ, nguyên tố cùng nhau, số 0 tận cùng", "đếm số không chia hết cho 5 và 7, phân số tối giản, số chính phương hoặc lập phương, số chữ số 0 tận cùng của n!", "số bội của p không vượt quá n là [n/p]; dùng bao hàm – loại trừ; số 0 tận cùng của n! = [n/5] + [n/25] + [n/125] + …", ["2013-3", "2014-20", "2017-16", "2019-6", "2025-5"]),
],
"2.1": [
 ("Tách 1/(n(n+1)) để khử liên tiếp", "tổng các phân số có mẫu là tích hai số liên tiếp hoặc cách đều (24 = 4 × 6, 40 = 5 × 8, n² − 1, n + n²)", "viết mỗi số hạng thành hiệu 1/a − 1/b rồi khử các số hạng giữa; mẫu dạng 1/a² − 1/b² cũng khử được", ["2022-4", "2022-5", "2025-1", "2025-6", "2023-1", "2024-7", "2014-14", "2017-9", "2013-16", "2011-15"]),
 ("Mẫu là tổng 1 + 2 + … + n", "mẫu số là tổng các số liên tiếp hoặc tổng bội của một số (31 + 62 + 93 + …)", "1 + 2 + … + n = n(n + 1)/2 nên 1/(1 + … + n) = 2(1/n − 1/(n + 1)), rồi khử liên tiếp", ["2015-16", "2021-11", "2022-7"]),
 ("Cấp số nhân và dãy Fibonacci", "tổng các lũy thừa của 2, phân số 1 − 1/2^k, tổng vô hạn có tử là dãy Fibonacci", "S × q − S để khử; với tổng Fibonacci F_n/7^n thì lấy S − S/7 − S/49 và dùng F_n = F_(n−1) + F_(n−2)", ["2009-13", "2010-5", "2015-2", "2019-20", "2022-17"]),
 ("Gom nhóm cùng mẫu, tích khử liên tiếp", "tổng các phân số k/n xếp theo nhóm, tích (1 + 1/k), tổng giai thừa đan dấu", "gom các phân số cùng mẫu (hoặc cùng tử) thành một số đẹp; (1 + 1/k) = (k + 1)/k nên tích khử; n! × (n + 2) = (n + 1)! + n! để khử tổng giai thừa", ["2017-1", "2024-10", "2022-1", "2012-16", "2012-7"]),
],
"2.2": [
 ("Đặt ẩn phụ cho tổng lặp lại", "biểu thức dạng (a + A)(A + b) − (a + A + b)·A với cùng một tổng dài xuất hiện nhiều lần", "đặt A là phần tổng chung, khai triển; mọi số hạng chứa A triệt tiêu, chỉ còn tích hai số đầu cuối", ["2010-11", "2019-12", "2023-3", "2025-11"]),
 ("Rút thừa số chung, số lặp khối", "phân số có các tích tỉ lệ (2×6×10 + 3×9×15 …), số lặp khối 191919, 20022002, số thập phân gấp đôi nhau", "191919 = 19 × 10101; rút thừa số chung ở tử và mẫu; đưa hỗn số và số thập phân về cùng một số rồi đặt thừa số chung", ["2009-4", "2009-11", "2012-2", "2011-5", "2015-4", "2016-1", "2008-2", "2017-3", "2018-4"]),
 ("Nhóm số hạng đan dấu, hiệu hai bình phương", "tổng có dấu thay đổi theo chu kỳ (+ + + − − −), tổng bình phương đan dấu, a² − b²", "nhóm theo chu kỳ dấu để mỗi nhóm có giá trị cố định; a² − b² = (a − b)(a + b) biến tổng bình phương thành tổng thường", ["2013-2", "2014-13", "2018-3", "2019-5", "2025-14", "2013-15", "2022-8"]),
 ("Phép toán mới, phân số liên tục, ước lượng", "định nghĩa phép toán *, ⊗; phân số nhiều tầng; tìm phần nguyên; so sánh phân số gần 1", "tính thử vài bước để thấy quy luật rồi khái quát; tính phân số liên tục từ tầng trong cùng; kẹp tổng giữa hai giá trị dễ tính; so sánh 1 − phân số", ["2012-12", "2015-1", "2014-5", "2023-5", "2011-4", "2018-18", "2019-1", "2019-4", "2013-5"]),
],
"3.1": [
 ("Tổng chữ số của 99…9 và các tích đặc biệt", "số gồm toàn chữ số 9 (hoặc 1, 2, 4), tích của chúng, tổng 9 + 99 + 999 + …", "viết 99…9 = 10^n − 1 rồi khai triển; thử với n nhỏ (n = 1, 2, 3) để thấy quy luật chữ số", ["2008-4", "2010-12", "2019-11", "2021-1", "2023-2", "2017-13", "2011-9"]),
 ("Đếm chữ số khi viết liên tiếp, chữ số thứ n", "viết liên tiếp các số lẻ, số chính phương, số đối xứng, bội của 5; hỏi số chữ số hoặc chữ số ở vị trí thứ n", "chia thành nhóm theo số chữ số (1, 2, 3 … chữ số), đếm số chữ số của từng nhóm rồi trừ dần để định vị", ["2010-7", "2011-19", "2015-8", "2021-14", "2024-18", "2025-15", "2012-1"]),
 ("Cấu tạo số: số chữ số, tổng chữ số cho trước, số lớn nhất – nhỏ nhất", "số nhỏ nhất có tổng chữ số cho trước, số chữ số của một tích, số lớn nhất và nhỏ nhất lập từ 4 chữ số", "muốn số nhỏ nhất thì dùng nhiều chữ số 9 nhất ở cuối; ước lượng số chữ số bằng lũy thừa của 10; viết số theo hàng (1000a + 100b + …) để lập phương trình", ["2010-4", "2013-1", "2014-18", "2019-18", "2023-20", "2009-20"]),
],
"3.2": [
 ("Bảng số xếp theo hàng, tam giác, xoắn ốc", "số được xếp thành hàng dài cố định, tam giác hay xoắn ốc; hỏi số ở dưới, ở trên hay hàng và cột của một số", "tìm số cuối của hàng k (k(k + 1)/2, 2^k, bình phương); hàng dài cố định thì dùng phép chia có dư để ra hàng và cột", ["2011-12", "2013-11", "2015-19", "2018-1", "2021-2", "2017-15"]),
 ("Quá trình lặp: tìm chu kỳ", "một thao tác lặp đi lặp lại (kéo công tắc, chia xu, quay mũi tên, kiến đi vòng, cho ăn theo luật); hỏi trạng thái sau rất nhiều bước", "mô phỏng vài vòng đầu để tìm trạng thái lặp lại, rồi dùng số dư của số bước cho độ dài chu kỳ", ["2009-10", "2012-8", "2018-7", "2018-9", "2019-15", "2016-5", "2015-10"]),
 ("Dãy số: tìm quy luật, số tam giác", "cho vài số hạng đầu, hỏi số hạng xa hoặc tổng; tháp cốc, que diêm; hộp có tổng 3 ô liên tiếp không đổi", "tính hiệu hoặc tỉ số giữa các số hạng liên tiếp; tổng 3 số liên tiếp không đổi thì dãy tuần hoàn chu kỳ 3; số tam giác n(n + 1)/2", ["2008-5", "2011-18", "2016-14", "2017-4", "2023-19", "2024-20", "2019-19"]),
],
"4.1": [
 ("Tỉ số thay đổi: giữ đại lượng không đổi", "thêm, bớt hay chuyển vật giữa các túi làm tỉ số thay đổi", "tìm đại lượng không đổi (phần không bị chuyển, tổng số) rồi quy các tỉ số về cùng số phần của đại lượng đó", ["2008-18", "2016-6", "2021-8", "2024-16", "2019-3", "2023-6", "2025-10", "2022-15", "2023-7"]),
 ("Phần trăm tăng giảm, lợi nhuận", "số lượng hoặc giá tăng giảm theo phần trăm, hỏi phần trăm hay số lượng ban đầu", "gọi số ban đầu là 100 phần (hoặc một ẩn), viết tổng sau khi thay đổi theo từng nhóm rồi so sánh", ["2009-6", "2013-19", "2017-20", "2022-9", "2024-14", "2023-12"]),
 ("Pha trộn dung dịch", "trộn hỗn hợp có tỉ lệ khác nhau, thêm nước hay chất tan", "đưa các hỗn hợp về cùng thể tích (hoặc cùng lượng chất không đổi), cộng từng thành phần rồi lập tỉ số", ["2012-19", "2013-6", "2024-17"]),
 ("Tính ngược từ cuối, lập phương trình", "ăn dần phân số của phần còn lại, đổi số lượng hai loại, mua hàng với nhiều món", "tính ngược từ kết quả cuối; hoặc gọi ẩn rồi lập phương trình, khử bớt món chưa biết bằng cách trừ hai phương trình", ["2008-9", "2011-3", "2012-3", "2021-7", "2009-2"]),
],
"4.2": [
 ("Gặp nhau và đuổi kịp, trên đường thẳng và đường tròn", "hai người đi ngược chiều hoặc cùng chiều, gặp nhau nhiều lần, quay đầu, chạy trên đường tròn", "quãng đường tổng hai người đi được giữa hai lần gặp liên tiếp là 2 lần quãng đường (đường tròn: 1 vòng); thời gian bằng nhau thì quãng đường tỉ lệ với vận tốc", ["2012-6", "2017-6", "2018-8", "2019-9", "2023-11", "2024-3", "2025-17", "2008-14", "2010-20", "2013-14", "2021-6", "2022-10"]),
 ("Dùng chung xe đạp, chở luân phiên", "chỉ có một xe đạp hoặc một xe chở được ít người, mọi người phải đến cùng lúc", "đến cùng lúc nên mỗi người đi bộ cùng một quãng đường; lập phương trình thời gian theo quãng đi xe và quãng đi bộ", ["2009-12", "2011-20", "2015-15", "2016-17", "2014-8"]),
 ("Kim đồng hồ", "góc giữa hai kim, hai kim thẳng hàng hay vuông góc, kim đối xứng qua một số", "kim phút đi 6°/phút, kim giờ đi 0,5°/phút, mỗi phút kim phút đuổi thêm 5,5°", ["2008-16", "2010-2", "2012-17", "2014-3", "2018-10"]),
 ("Năng suất công việc", "nhiều người làm chung một việc, nghỉ giữa chừng, năng suất giảm khi làm chung", "năng suất = 1 / thời gian làm một mình; cộng năng suất khi làm chung; chọn tổng công việc là BCNN các thời gian để tránh phân số", ["2008-20", "2009-15", "2012-9", "2019-16", "2022-11", "2025-18"]),
],
"5.1": [
 ("Tỉ số diện tích tam giác chung đường cao", "tam giác bị chia bởi các đoạn nối từ đỉnh, cho tỉ số cạnh hoặc diện tích vài phần", "hai tam giác chung đường cao thì tỉ số diện tích bằng tỉ số đáy; đi lần lượt từ phần đã biết sang phần chưa biết, có thể đặt ẩn cho một phần", ["2011-16", "2012-14", "2013-9", "2018-14", "2023-18", "2024-2", "2016-19", "2008-17"]),
 ("Hình chữ nhật, hình thang: tam giác bướm", "hình chữ nhật hoặc hình thang có các đường chéo, điểm nằm trong hay trên cạnh", "tam giác có đáy là cạnh và đỉnh trên cạnh đối diện bằng nửa hình chữ nhật; trong hình thang hai tam giác bên bằng nhau và tỉ số các phần theo tỉ số hai đáy", ["2010-14", "2018-16", "2019-7", "2015-12", "2017-14", "2009-14"]),
 ("Tam giác đồng dạng, dải song song", "các đường song song với một cạnh chia tam giác thành dải, hình bình hành nằm trong tam giác", "tỉ số diện tích bằng bình phương tỉ số đồng dạng; tam giác bị chia thành n dải đều có diện tích theo tỉ lệ 1 : 3 : 5 : …", ["2012-18", "2019-17", "2022-16", "2023-15", "2021-15"]),
 ("Cắt ghép, đối xứng, hình vuông lồng nhau", "hình vuông nối trung điểm lồng nhau, ngôi sao trong ngũ giác, dải chéo trong hình vuông, tìm điểm trên lưới", "chia hình thành các mảnh bằng nhau; mỗi lần nối trung điểm thì diện tích giảm một nửa; dùng tính đối xứng của hình", ["2021-4", "2016-8", "2025-7", "2014-1", "2011-13"]),
],
"5.2": [
 ("Thêm bớt hình: cộng trừ các phần chồng nhau", "phần tô màu tạo bởi nhiều nửa hình tròn, hình quạt, hình tròn nằm trong nhau", "viết phần tô màu thành tổng – hiệu của các hình quen thuộc (quạt, nửa hình tròn, tam giác); phần chung bị cộng hai lần thì trừ bớt", ["2008-8", "2009-7", "2011-10", "2012-4", "2017-12", "2025-9", "2018-2", "2016-11", "2022-6"]),
 ("Tổng các hình quạt: tổng góc ở tâm", "các hình quạt cùng bán kính có tâm ở các đỉnh của một đa giác", "ghép các hình quạt lại; tổng góc ở tâm bằng tổng góc của đa giác (n − 2) × 180° hoặc 360°", ["2019-8", "2021-5"]),
 ("Chu vi, cung tròn, hình tròn lăn", "hỏi chu vi đường viền tạo bởi các cung, hoặc diện tích quét khi hình tròn lăn theo cạnh hình vuông", "độ dài cung = (góc/360°) × 2πr, cộng các cung theo góc ở tâm; hình tròn lăn quét một dải cộng thêm các góc bo tròn", ["2014-2", "2015-5", "2017-8", "2023-8"]),
 ("Hình viên phân, tam giác đều trong hình tròn", "các hình tròn đi qua tâm của nhau, đường tròn tiếp xúc với cạnh hình quạt", "nối các tâm thành tam giác đều (góc 60°); viên phân = quạt − tam giác; tam giác nửa đều có cạnh đối diện góc 30° bằng nửa cạnh huyền", ["2010-6", "2014-12"]),
],
"5.3": [
 ("Tổng góc hình sao, chuỗi tam giác cân", "hình sao nhiều cánh, các đoạn bằng nhau dựng nối tiếp trên hai tia của một góc", "góc ngoài tam giác bằng tổng hai góc trong không kề; tổng các góc ở đỉnh sao 7 cánh vẽ cách 2 đỉnh = 180°; chuỗi tam giác cân thì góc tăng dần đều", ["2010-10", "2024-19", "2009-17", "2015-17", "2013-18"]),
 ("Góc trong đa giác đều, tam giác cân, đường vuông góc", "ghép ngũ giác đều với hình vuông, tam giác đều; hình bình hành có các cạnh bằng nhau", "góc ngũ giác đều 108°, lục giác đều 120°; tìm các cặp cạnh bằng nhau để có tam giác cân rồi tính góc đáy", ["2019-14", "2022-18", "2025-8", "2016-10", "2017-2"]),
 ("Hình lập phương: sơn mặt, diện tích bề mặt, ghép khối", "khối lập phương nhỏ được sơn, khoan lỗ, xếp từ hình chiếu; hình khai triển của lập phương", "đếm theo vị trí (đỉnh, cạnh, mặt, bên trong); diện tích bề mặt = mặt ngoài − lỗ + mặt trong lỗ; nhìn hình khai triển để tìm mặt đối diện", ["2009-1", "2016-9", "2021-13", "2021-19", "2011-6", "2016-3"]),
 ("Độ dài và diện tích qua cắt ghép, bi-a phản xạ", "tìm cạnh hình vuông từ các đoạn thẳng, hình vuông nội tiếp tam giác, bóng nảy trên bàn", "dựng thêm tam giác vuông cân hoặc hình chữ nhật phụ để chuyển độ dài; bóng nảy thì trải phẳng bàn thành lưới và đi theo đường thẳng", ["2010-19", "2016-12", "2024-9", "2024-11", "2023-14", "2012-11", "2014-11"]),
],
"6.1": [
 ("Chia vật giống nhau, đếm tổ hợp số tiền", "chia kẹo, xu, hộp giống nhau cho vài người với số tối thiểu; đếm cách trả tiền hay chọn ba số có tổng cho trước", "trước hết phát đủ số tối thiểu, rồi chia phần còn lại (chia n vật cho k người, mỗi người ít nhất 1: C(n − 1, k − 1)); số tờ tiền ít thì liệt kê theo tờ lớn nhất", ["2008-7", "2015-18", "2018-19", "2023-17", "2019-13", "2014-6", "2022-20"]),
 ("Lập số từ chữ số cho trước, đếm số có tính chất chữ số", "lập số từ các chữ số của năm thi, số có chữ số giảm dần, tích hay tổng chữ số cho trước", "đếm theo từng vị trí bằng quy tắc nhân; chú ý chữ số 0 không đứng đầu và chữ số lặp lại; tích chữ số thì phân tích ra thừa số rồi phân phối vào các chữ số", ["2010-15", "2012-10", "2017-5", "2019-2", "2016-16", "2016-18", "2021-9", "2025-13"]),
 ("Chọn số theo số dư để tổng chia hết", "chọn 2 hoặc 3 số trong một dãy liên tiếp sao cho tổng chia hết cho 3 hoặc 4", "chia các số thành nhóm theo số dư, liệt kê các bộ số dư có tổng chia hết rồi nhân số cách chọn trong từng nhóm", ["2015-14", "2017-11", "2022-14"]),
 ("Xếp có ràng buộc, tô màu, hoán vị không đúng chỗ", "tô màu sao cho hai ô kề nhau khác màu, mũ khác màu cạnh nhau, trả bài sai người, đối xứng", "đếm lần lượt theo thứ tự hợp lý, bắt đầu từ chỗ ràng buộc nhiều nhất; hoán vị không đúng chỗ của n phần tử: D_2 = 1, D_3 = 2, D_4 = 9", ["2009-8", "2014-17", "2016-2", "2018-11", "2022-13", "2013-12", "2010-16", "2012-15", "2021-18"]),
],
"6.2": [
 ("Đếm tam giác, giao điểm từ các điểm cho trước", "các điểm trên đường tròn hoặc trên vài đường thẳng; hỏi số tam giác, tam giác vuông, giao điểm, đường thẳng", "chọn 3 điểm bất kỳ rồi trừ các bộ ba thẳng hàng; tam giác vuông nội tiếp có cạnh huyền là đường kính; mỗi giao điểm ứng với 4 điểm", ["2008-15", "2019-10", "2010-13", "2024-4", "2009-19", "2024-13"]),
 ("Đếm hình trong lưới, trong hình vẽ", "đếm hình vuông, tam giác trong lưới hay trong một hình vẽ có nhiều đường", "đếm theo kích thước (1 × 1, 2 × 2, …) hoặc theo đỉnh/cạnh; phần bị khuyết thì trừ các hình chứa nó", ["2008-10", "2009-3"]),
 ("Đường đi: cộng dồn số cách ở mỗi nút", "chỉ được đi sang phải, xuống dưới, theo đường chéo; đọc chữ số trên bảng; đi rồi quay về chỗ cũ", "ghi số cách đến mỗi nút bằng tổng số cách đến các nút ngay trước nó, đi dần tới đích", ["2009-18", "2011-8", "2013-7", "2013-13", "2018-6"]),
 ("Truy hồi kiểu bậc thang", "mỗi lần đi 1, 2 hoặc 3 bậc, ăn 1 hoặc 2 thanh kẹo", "số cách với n bậc = tổng số cách với n − 1, n − 2 (, n − 3) bậc; tính dần từ n nhỏ", ["2011-11", "2015-11"]),
],
"6.3": [
 ("Dirichlet: trường hợp xấu nhất", "hỏi phải lấy ít nhất (hay tối đa phải thử) bao nhiêu lần để chắc chắn có kết quả", "dựng trường hợp xui xẻo nhất (lấy hết những thứ không cần trước), rồi cộng thêm 1", ["2009-5", "2015-6", "2017-18", "2024-15", "2025-20"]),
 ("Cực trị: chặn rồi dựng ví dụ", "tìm giá trị nhỏ nhất hay lớn nhất (tổng điểm, số người, số cuộc gọi, phần chung nhỏ nhất trong biểu đồ Venn)", "chứng minh một chặn trên/dưới (thường bằng cách cộng hoặc so sánh), rồi chỉ ra một ví dụ đạt đúng chặn đó; phần chung ít nhất = tổng − (số môn − 1) × tổng số người", ["2008-1", "2009-9", "2025-2", "2012-20", "2013-8", "2010-1", "2011-2", "2014-16", "2021-10", "2013-10", "2018-5", "2023-13"]),
 ("Suy luận logic, điền bảng", "ai nói dối, ai làm ngày nào, đồng xu dưới quân nào; điền số vào bảng theo điều kiện", "giả sử từng trường hợp rồi tìm mâu thuẫn; bắt đầu từ điều kiện chặt nhất; ghi lại thông tin mỗi câu trả lời loại bỏ được", ["2008-11", "2017-7", "2025-3", "2024-8", "2025-19"]),
 ("Trò chơi bốc vật: vị trí thắng", "hai người lần lượt bốc kẹo hoặc xu theo luật, hỏi nước đi đầu tiên để thắng", "tìm các vị trí thua (người đến lượt sẽ thua) bằng cách đi ngược từ cuối; với luật bốc 1 đến k vật thì vị trí thua cách nhau k + 1", ["2015-20", "2016-20"]),
],
}
