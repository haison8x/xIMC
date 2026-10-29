# Technique leaves for the SASMO mind map: sub-group -> [(title, sign, key, [example problem ids])].
# Few, broad leaves on purpose, so that every leaf collects several problems.
GROUP_VN = {
 1: ("Số & chữ số", "Numbers & Digits"),
 2: ("Quy luật", "Patterns"),
 3: ("Toán có lời văn", "Word Problems"),
 4: ("Hình học & không gian", "Geometry & Spatial"),
 5: ("Đếm & logic", "Counting & Logic"),
}
SUB_VN = {
 "1.1": "Tính nhanh, giá trị theo hàng & câu số", "1.2": "Chia hết, bội & ước",
 "1.3": "Chữ số, tìm số bí ẩn & phép tính chữ",
 "2.1": "Dãy số & hình lớn dần", "2.2": "Phép toán bí ẩn, số trong hình & quy luật hình ảnh",
 "3.1": "Tổng – hiệu, chuyển bớt, tuổi, giả thiết tạm & biểu đồ tranh", "3.2": "Thời gian, lịch, đo lường & số khoảng",
 "3.3": "Đại lượng ẩn: hình thay số, cân thăng bằng & tính ngược",
 "4.1": "Chu vi & diện tích", "4.2": "Đếm hình, khối lập phương & đồ vật",
 "4.3": "Đố không gian & thị giác: ảnh gương, hình chiếu, khai triển, gấp giấy",
 "5.1": "Đếm cách chọn & đếm số", "5.2": "Logic, điền số, Dirichlet & cực trị",
}
L = {
"1.1": [
 ("Cộng nhiều số: ghép cặp tròn chục, tròn trăm", "tổng dài nhiều số hạng lẻ tẻ, có cả cộng lẫn trừ", "ghép các số có tổng (hoặc hiệu) tròn chục, tròn trăm; gom các số trừ lại trừ một lần", ["2019-G3-1", "2020-G3-1", "2024-G3-1", "2017-G3-1", "2024-G1-1"]),
 ("Hàng chục, hàng đơn vị & câu số có ô trống", "\"… là 3 chục 7 đơn vị kém 4 chục 6 đơn vị\", điền số vào ô trống để hai vế bằng nhau", "đổi chục – đơn vị ra số rồi cộng trừ; câu số thì tính hết vế đã biết, rồi dùng phép tính ngược để tìm ô trống", ["2015-G3-5", "2017-G3-2", "2020-G3-2", "2024-G1-2", "2024-G1-4", "2013-PR-1", "2013-PR-2", "2014-G3-3", "2019-G3-20"]),
 ("Tổng dãy cách đều, tổng đan dấu", "cộng các số lẻ liên tiếp, các số giảm đều, tổng + − xen kẽ, nhiều số hạng giống nhau", "tổng dãy cách đều = (số đầu + số cuối) × số số hạng : 2; tổng đan dấu thì ghép từng cặp liền nhau; nhiều số giống nhau thì đổi thành phép nhân", ["2016-G3-17", "2018-G3-16", "2020-G3-16", "2013-PR-38"]),
 ("Tính chất phép tính, phép toán cho công thức, so sánh phân số", "nhân với 0, phép toán mới có công thức cho sẵn, lũy thừa, so sánh phần đã ăn của các chiếc bánh, tích có 25 và 125", "dùng tính chất phân phối và giao hoán; thay số vào đúng công thức; so sánh phần còn lại (1 − phân số); ghép 4 × 25, 8 × 125 cho tròn", ["2016-G3-1", "2015-G3-6", "2014-G3-4", "2015-G3-2", "2017-G3-7", "2024-G2-11", "2013-PR-37"]),
],
"1.2": [
 ("Dấu hiệu chia hết cho 2, 3, 6, 9, 11: tìm chữ số ẩn", "số có một chữ số bị che, hỏi chữ số đó để số chia hết hoặc có số dư cho trước", "chia hết cho 3 / 9 thì xét tổng các chữ số; cho 11 thì xét hiệu tổng chữ số hàng lẻ và hàng chẵn; cho 6 thì vừa chẵn vừa chia hết cho 3", ["2015-G3-12", "2016-G3-11", "2019-G3-8", "2020-G3-9", "2014-G3-14", "2024-G2-6", "2024-G3-5", "2024-G3-11", "2024-G1-3"]),
 ("Đếm bội trong một khoảng", "hỏi có bao nhiêu số chia hết cho a (hoặc cho cả a và b) nằm giữa hai số", "đếm bội đầu tiên và bội cuối cùng trong khoảng; số bội = (cuối − đầu) : a + 1; chia hết cho cả a và b thì là bội của BCNN(a, b)", ["2016-G3-12", "2019-G3-14", "2020-G3-5", "2024-G2-3"]),
 ("Bội chung, ước, số chính phương", "số vừa là bội của 3 và 7, lớn hơn bội của 13 một đơn vị; tích hai trang sách liền nhau; số chính phương; chia đều xúc xích", "liệt kê các bội chung trong khoảng rồi lọc theo điều kiện chẵn lẻ; phân tích ra thừa số để tìm cặp số hay số cần nhân thêm để thành số chính phương", ["2015-G3-9", "2016-G3-23", "2017-G3-14", "2018-G3-19", "2015-G3-13", "2013-PR-3", "2013-PR-4", "2014-G3-2", "2014-G3-11"]),
],
"1.3": [
 ("Phép tính chữ: mỗi chữ cái là một chữ số", "phép cộng, trừ, nhân đặt theo cột với các chữ cái khác nhau là các chữ số khác nhau", "bắt đầu từ cột có nhớ hoặc từ chữ số đầu của kết quả (tổng hai số có 3 chữ số ra 4 chữ số thì chữ số đầu là 1); thử các trường hợp còn lại", ["2014-G3-16", "2015-G3-17", "2016-G3-25", "2017-G3-24", "2018-G3-24", "2019-G3-25", "2020-G3-25", "2024-G2-25", "2024-G3-24", "2013-PR-23"]),
 ("Tìm số theo manh mối, số lớn nhất có tổng chữ số cho trước", "\"Tôi là số có 3 chữ số …\", số lớn nhất lẻ/chẵn có tổng chữ số cho trước, hiệu lớn nhất của hai số đảo ngược chữ số", "viết số thành các chữ số a b c rồi dùng manh mối chặt nhất trước; muốn số lớn nhất thì để chữ số lớn nhất ở hàng cao, kiểm tra chữ số cuối theo điều kiện chẵn lẻ", ["2019-G3-21", "2024-G1-21", "2024-G2-20", "2024-G3-21", "2024-G1-20", "2024-G2-18", "2024-G3-16", "2013-PR-8"]),
 ("Đếm chữ số khi viết dãy số", "viết các số từ 1 đến n, các số lẻ, bội của 5; hỏi có bao nhiêu chữ số, bao nhiêu chữ số 1 (5), hay số thứ n chỉ dùng chữ số lẻ", "đếm riêng nhóm 1 chữ số, 2 chữ số, 3 chữ số; đếm chữ số 1 lần lượt ở hàng đơn vị, hàng chục, hàng trăm", ["2016-G3-24", "2017-G3-22", "2019-G3-23", "2024-G2-19", "2014-G3-19", "2020-G3-10"]),
],
"2.1": [
 ("Dãy có hiệu tăng (giảm) đều", "hiệu giữa hai số liền nhau là 1, 2, 3, 4 … hoặc giảm dần", "viết hàng hiệu bên dưới dãy; hiệu tạo thành dãy đơn giản thì cộng tiếp để ra số sau", ["2015-G3-1", "2017-G3-4", "2024-G1-9", "2024-G2-5", "2013-PR-15", "2013-PR-32"]),
 ("Dãy nhân rồi cộng, dãy xen kẽ hai quy luật", "các số tăng rất nhanh (gấp đôi, gấp ba, nhân với số thứ tự) hoặc lên xuống xen kẽ", "thử số sau = số trước × k + c hoặc × số thứ tự; dãy xen kẽ thì tách các số ở vị trí lẻ và vị trí chẵn thành hai dãy", ["2014-G3-6", "2020-G3-8", "2024-G3-3", "2016-G3-8", "2018-G3-6", "2013-PR-43"]),
 ("Hình lớn dần và bảng số", "dãy hình làm bằng que, viên gạch, ô đen lớn dần; số xếp thành bảng nhiều hàng", "đếm số đối tượng ở 3–4 hình đầu, tìm phần thêm vào mỗi lần rồi lập công thức theo số thứ tự của hình; bảng số thì tìm quy luật theo hàng", ["2014-G3-10", "2013-PR-13", "2013-PR-19"]),
],
"2.2": [
 ("Phép toán bí ẩn đoán từ ví dụ", "cho vài ví dụ a ✡ b = …, hoặc số trên hộp biến thành số dưới, hỏi kết quả của một cặp mới", "thử các phép kết hợp đơn giản (a × b, a + b, ghép chữ số, a × b × 2…) rồi kiểm tra với mọi ví dụ trước khi dùng", ["2015-G3-3", "2017-G3-15", "2019-G3-17", "2013-PR-39", "2024-G1-16", "2024-G3-13"]),
 ("Số trong hình: quan hệ giữa các ô", "số trong các phần của tam giác, ngũ giác, hình lồng nhau, đồng hồ, lưới có tim; tìm số còn thiếu", "tìm phép tính nối các ô ở mỗi hình (tích hai góc, tổng nhân 2, đếm cạnh của hình bao quanh…) rồi áp dụng cho hình có dấu ?", ["2017-G3-21", "2018-G3-21", "2024-G1-22", "2024-G3-25", "2019-G3-24"]),
 ("Quy luật hình ảnh trong bảng 3 × 3", "bảng hình (mặt cười, ngôi sao, chấm đen trắng) có một ô trống", "xét từng đặc điểm riêng (số tóc, kiểu miệng, vị trí ngôi sao, số chấm): mỗi hàng và mỗi cột thường có đủ mọi kiểu, hoặc đặc điểm xoay vòng theo chiều kim đồng hồ", ["2018-G3-14", "2019-G3-2", "2019-G3-11", "2020-G3-3"]),
],
"3.1": [
 ("Chuyển bớt giữa hai nhóm, tổng – hiệu", "chuyển bút, trứng, sách từ nhóm này sang nhóm kia; biết tổng và hiệu (hoặc gấp mấy lần) của các nhóm", "chuyển k vật thì hiệu thay đổi 2k; số lớn = (tổng + hiệu) : 2; dùng sơ đồ đoạn thẳng (mô hình phần)", ["2014-G3-13", "2016-G3-19", "2018-G3-15", "2018-G3-18", "2017-G3-23", "2024-G1-17", "2024-G2-13", "2024-G3-9", "2024-G3-18", "2013-PR-30", "2019-G3-19"]),
 ("Bài toán tuổi", "tuổi hiện nay, mấy năm trước hoặc mấy năm sau, tổng tuổi hay gấp mấy lần", "hiệu tuổi không bao giờ thay đổi; mỗi năm tổng tuổi tăng thêm số người; vẽ sơ đồ ở thời điểm có tỉ số", ["2014-G3-1", "2017-G3-20", "2024-G1-24", "2024-G2-22", "2013-PR-26", "2013-PR-33"]),
 ("Giả thiết tạm: gà – thỏ, vé người lớn – trẻ em", "biết tổng số con và tổng số chân, tổng số người và tổng số tiền, số hộp to nhỏ", "giả sử tất cả đều là loại thứ nhất, tính phần thiếu (thừa) rồi chia cho chênh lệch của mỗi con; số ít thì thử từng khả năng", ["2013-PR-29", "2013-PR-44", "2024-G2-23", "2019-G3-22", "2015-G3-18", "2013-PR-35", "2014-G3-18"]),
 ("Biểu đồ tranh, bảng số liệu, đổi vỏ lấy hàng", "mỗi hình trong biểu đồ ứng với cùng một số đồ vật; bảng điểm; đổi k vỏ lấy 1 sản phẩm", "tìm giá trị của một hình từ tổng (hoặc hiệu) đã biết rồi nhân lên; đổi vỏ thì mỗi lần đổi k vỏ mất đi k − 1 vỏ, nhớ tận dụng vỏ của chai mới", ["2016-G3-20", "2017-G3-18", "2019-G3-18", "2024-G2-16", "2024-G3-6", "2020-G3-19", "2018-G3-3", "2014-G3-8", "2024-G3-7"]),
],
"3.2": [
 ("Thứ trong tuần và lịch tháng", "ngày thứ n kể từ một thứ đã biết, tháng bắt đầu và kết thúc vào thứ mấy, ngày cuối cùng trong tháng", "cứ 7 ngày lặp lại một thứ: lấy số ngày chia 7 rồi xét số dư; tháng 28, 29, 30, 31 ngày thì thứ của ngày cuối lệch 0, 1, 2, 3 so với ngày đầu", ["2015-G3-14", "2016-G3-3", "2016-G3-13", "2017-G3-3", "2018-G3-11", "2019-G3-13", "2020-G3-4", "2024-G1-18", "2024-G2-14", "2013-PR-11"]),
 ("Khoảng thời gian và đồng hồ", "giờ đi, giờ về, lịch chiếu phim, số độ kim phút quay, đổi tuần ra phút", "tính qua mốc giờ tròn; kim phút quay 6° mỗi phút; đổi đơn vị theo từng bước (tuần → ngày → giờ → phút)", ["2016-G3-16", "2019-G3-10", "2020-G3-7", "2013-PR-17", "2016-G3-4"]),
 ("Số khoảng: trồng cây, cưa gỗ, leo tầng", "đèn hai bên sông, lính đứng hai bên đường, cưa ống thành nhiều đoạn, đi từ tầng này lên tầng khác", "số khoảng = số cây − 1 (đường thẳng có cây ở hai đầu); số nhát cưa = số đoạn − 1; từ tầng a lên tầng b là b − a tầng", ["2014-G3-7", "2016-G3-6", "2018-G3-5", "2020-G3-14"]),
 ("Đo lường, tốc độ, năng suất", "đổi đơn vị độ dài, so chiều cao đồ vật theo vạch kẻ, đi bao xa trong thời gian cho trước, nhiều thợ cùng làm", "đổi về cùng một đơn vị; giữ đúng tỉ lệ (gấp đôi thời gian thì gấp đôi quãng đường); nhiều người làm song song không làm một xe chạy nhanh hơn", ["2016-G3-2", "2018-G3-2", "2013-PR-9", "2013-PR-10", "2013-PR-16", "2024-G1-5", "2024-G2-1"]),
],
"3.3": [
 ("Hình thay số, cân thăng bằng", "các phương trình viết bằng hình (con vật, trái cây, viên đá quý), cân thăng bằng, khinh khí cầu chở các con vật", "so sánh hai phương trình (hai cân) chỉ khác nhau một hình để tìm ra hình đó, rồi thay ngược vào; đổi mọi thứ ra cùng một loại", ["2013-PR-34", "2017-G3-8", "2017-G3-16", "2018-G3-23", "2019-G3-9", "2019-G3-15", "2024-G1-19", "2024-G2-17", "2024-G3-17"]),
 ("Tính ngược từ kết quả", "một chuỗi phép tính (cộng, trừ, nhân, chia) ra kết quả cho trước, hỏi số ban đầu", "đi ngược từ cuối lên đầu và làm phép tính ngược ở mỗi bước (cộng ↔ trừ, nhân ↔ chia)", ["2017-G3-9", "2018-G3-20", "2020-G3-20"]),
 ("So sánh hai trường hợp để khử bớt", "thùng chứa hai lượng nước khác nhau, mua nhiều món với giá ghép từng cặp", "lấy hai trường hợp trừ nhau để mất phần chung (vỏ thùng, một món hàng) rồi tìm phần còn lại", ["2020-G3-13", "2020-G3-22"]),
],
"4.1": [
 ("Chu vi hình ghép từ ô vuông và hình chữ nhật", "hình bậc thang, kim tự tháp ô vuông, hình chữ nhật ghép từ nhiều hình nhỏ giống nhau", "dời các cạnh bậc thang ra ngoài thành hình chữ nhật bao quanh; hoặc đếm số cạnh ô vuông nằm trên đường viền rồi nhân với độ dài một cạnh", ["2015-G3-4", "2016-G3-22", "2018-G3-13", "2019-G3-12", "2024-G3-8", "2020-G3-17", "2013-PR-28", "2014-G3-5"]),
 ("Diện tích phần tô màu, chia hình", "hình vuông hay hình chữ nhật chia thành các phần, phần tô màu là tam giác hoặc tứ giác", "chia phần tô màu thành các tam giác có đáy và chiều cao dễ đọc trên lưới; hoặc lấy cả hình trừ đi các phần không tô", ["2017-G3-12", "2020-G3-21", "2024-G3-20", "2015-G3-20", "2013-PR-24", "2013-PR-25"]),
 ("Xếp hình, hình tròn, thể tích", "cắt hình chữ nhật nhỏ từ tờ giấy lớn, ghép hình vuông lớn nhất, hình tròn nội tiếp, đếm khối lập phương nhỏ lấp đầy hộp", "chia mỗi chiều cho cạnh hình nhỏ rồi nhân; hình vuông lớn nhất từ n ô thì cạnh là số lớn nhất có bình phương không vượt n", ["2015-G3-10", "2015-G3-15", "2013-PR-20", "2013-PR-21", "2013-PR-22", "2016-G3-5"]),
],
"4.2": [
 ("Đếm tam giác, hình vuông, hình chữ nhật", "hình có nhiều đường kẻ cắt nhau, hỏi có bao nhiêu tam giác (hình vuông, hình chữ nhật)", "đếm có hệ thống: theo kích thước (1 ô, 2 ô, …) hoặc theo số phần ghép lại; hình chữ nhật trong dải thì đếm số cách chọn hai đường kẻ", ["2014-G3-17", "2015-G3-8", "2016-G3-9", "2017-G3-17", "2018-G3-17", "2019-G3-16", "2020-G3-18", "2024-G1-12", "2024-G2-9", "2024-G3-19", "2013-PR-42"]),
 ("Đếm khối lập phương xếp ở góc phòng", "các khối lập phương chồng lên nhau trong góc tường, không có lỗ hổng phía sau", "đếm theo từng cột (ghi chiều cao của mỗi cột lên hình nhìn từ trên xuống) rồi cộng lại, hoặc đếm theo từng tầng", ["2017-G3-13", "2018-G3-12", "2020-G3-6", "2024-G1-10", "2024-G2-7", "2024-G3-4"]),
 ("Đếm chấm, viên gạch, đồ vật", "đếm chấm trong hình, trái tim xếp hình vương miện, số viên gạch cần để vá bức tường", "chia hình thành các phần đối xứng hoặc các hàng rồi đếm từng phần; với tường thì đếm số viên mỗi hàng còn thiếu", ["2018-G3-1", "2024-G1-6", "2024-G2-2", "2024-G1-8", "2024-G3-2"]),
],
"4.3": [
 ("Ảnh gương, bóng, tìm hình giống hệt", "chọn ảnh trong gương, bóng của con vật, hình giống hệt hình mẫu hay hình khác loại", "so từng chi tiết nhỏ với hình mẫu và loại dần; ảnh gương đổi trái thành phải, đồng hồ trong gương phải lật lại", ["2017-G3-6", "2019-G3-7", "2018-G3-10", "2017-G3-11", "2024-G1-7", "2024-G2-4", "2024-G2-15"]),
 ("Hình khai triển, hình chiếu, xoay khối", "gấp hình khai triển thành con xúc xắc hay kim tự tháp, nhìn khối từ trên xuống, xoay khối", "trong hình khai triển, hai mặt cách nhau một ô trên cùng một hàng là hai mặt đối diện; hình chiếu từ trên chỉ thấy mặt trên của mỗi khối", ["2016-G3-10", "2020-G3-15", "2019-G3-4", "2016-G3-15"]),
 ("Gấp cắt giấy, mảnh còn thiếu, ghép hình", "gấp tờ giấy nhiều lần rồi cắt; chọn mảnh vừa chỗ trống trong hình kẻ sọc; hình nào ghép được thành hình chữ nhật", "mở dần từng nếp gấp (vết cắt đối xứng qua mỗi nếp); mảnh còn thiếu phải khớp cả khoảng cách lẫn vị trí các đường kẻ", ["2024-G1-15", "2024-G3-14", "2024-G1-11", "2024-G2-8", "2018-G3-9"]),
],
"5.1": [
 ("Quy tắc nhân, chọn 2 từ n", "chọn một vị bánh và một loại kem, chọn 2 màu khác nhau, bắt tay, đấu cờ vòng tròn", "chọn lần lượt từng bước thì nhân số cách; chọn 2 thứ không kể thứ tự từ n thì có n × (n − 1) : 2 cách", ["2017-G3-10", "2019-G3-6", "2015-G3-7", "2018-G3-7", "2014-G3-9", "2024-G3-10"]),
 ("Đếm số có chữ số theo điều kiện", "số đối xứng, số chỉ gồm chữ số chẵn (lẻ), chữ số giảm dần, số tạo từ các chữ số cho trước chia hết cho 4", "đếm số cách chọn cho từng hàng rồi nhân; chữ số 0 không đứng đầu; điều kiện chia hết thì chọn hai chữ số cuối trước", ["2013-PR-7", "2018-G3-8", "2024-G1-23", "2024-G2-21", "2013-PR-45", "2024-G3-22"]),
 ("Số làm bằng que diêm", "mỗi chữ số cần một số que (1 cần 2 que, 8 cần 7 que…), hỏi số lớn nhất hay đếm số có tổng số que chẵn hoặc lẻ", "ghi số que của từng chữ số; muốn số lớn nhất thì dùng nhiều chữ số nhất (nhiều số 1); điều kiện chẵn lẻ thì chia chữ số theo số que chẵn hay lẻ", ["2024-G1-25", "2024-G2-24", "2024-G3-23", "2020-G3-23"]),
],
"5.2": [
 ("Suy luận: ai là ai, thứ tự, ngồi quanh bàn", "vài người với nghề nghiệp, tuổi, cân nặng hay đồ vật khác nhau; một người nói dối; xếp hàng hoặc ngồi quanh bàn tròn", "lập bảng người × thuộc tính, điền chắc chắn từ manh mối mạnh nhất rồi loại dần; có người nói dối thì thử lần lượt từng người", ["2016-G3-21", "2017-G3-19", "2019-G3-5", "2020-G3-11", "2024-G1-13", "2024-G2-10", "2024-G1-14", "2024-G2-12", "2015-G3-16", "2013-PR-41", "2014-G3-20", "2024-G3-15"]),
 ("Điền số vào hình", "ô vuông Latin (mỗi hàng, mỗi cột không lặp), tổng trên mỗi đường bằng nhau, ô số kiểu dò mìn, lật thẻ", "bắt đầu từ ô có ít khả năng nhất; số ở giữa thuộc nhiều đường nên quyết định tổng; thử rồi kiểm tra lại toàn bộ", ["2016-G3-14", "2017-G3-5", "2017-G3-25", "2018-G3-25", "2020-G3-24", "2016-G3-18"]),
 ("Dirichlet: trường hợp xấu nhất", "lấy bóng, xe đồ chơi mà không nhìn, thử chìa khóa (bản đồ); hỏi ít nhất bao nhiêu lần để chắc chắn", "dựng trường hợp xui nhất (lấy tối đa mà vẫn chưa đạt yêu cầu) rồi cộng thêm 1", ["2013-PR-5", "2018-G3-22", "2024-G3-12"]),
 ("Cực trị và vị trí trong hàng", "giá trị lớn nhất – nhỏ nhất, chia vật sao cho đống lớn nhất nhỏ nhất, vị trí thứ mấy từ đầu và từ cuối hàng", "đẩy các số về phía có lợi rồi kiểm tra điều kiện; số người trong hàng = vị trí từ đầu + vị trí từ cuối − 1", ["2013-PR-6", "2013-PR-18", "2014-G3-15", "2015-G3-11", "2014-G3-12", "2019-G3-3", "2013-PR-14", "2018-G3-4", "2013-PR-36"]),
],
}
