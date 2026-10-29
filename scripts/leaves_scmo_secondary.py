# Technique leaves for the SCMO secondary mind map: sub-group -> [(title, sign, key, [example problem ids])].
# Few, broad leaves on purpose, so that every leaf collects several problems.
GROUP_VN = {
 1: ("Đại số", "Algebra"),
 2: ("Số học", "Number Theory"),
 3: ("Hình học", "Geometry"),
 4: ("Tổ hợp", "Combinatorics"),
}
SUB_VN = {
 "1.1": "Lũy thừa, căn thức, phân số & giá trị tuyệt đối", "1.2": "Phương trình, hệ, Vieta & hàm số",
 "1.3": "Cực trị & bất đẳng thức: bình phương, giá trị tuyệt đối, AM-GM",
 "2.1": "Số nguyên tố, phân tích nhân tử & phương trình nghiệm nguyên",
 "2.2": "Chia hết, số dư, chữ số & phần nguyên",
 "3.1": "Góc", "3.2": "Độ dài, diện tích & tam giác đồng dạng",
 "4.1": "Đếm, logic & cực trị rời rạc",
}
L = {
"1.1": [
 ("Lũy thừa và so sánh lũy thừa", "tích các lũy thừa, so sánh a^110 với b^88, số mũ 0 và số mũ âm", "đưa về cùng số mũ (hoặc cùng cơ số) rồi so sánh; nhóm a^m b^n từ các biểu thức đã biết", ["2023-S1-1", "2026-SJ-1", "2025-SJ-1", "2022-SJ-1"]),
 ("Căn thức: căn lồng nhau, liên hợp, căn bậc ba", "căn trong căn, tổng hai căn liên hợp, 26 + 15√3", "viết biểu thức dưới căn thành bình phương (lập phương) đúng: a ± 2√b = (√x ± √y)^2; nhân liên hợp; điều kiện xác định của căn chặn được biến", ["2022-SA-1", "2022-SA-4", "2023-S1-12", "2026-SA-3", "2026-SJ-3"]),
 ("Tổng phân số, thay giá trị, hàm dấu, tích sin", "tổng tách được thành hiệu, hệ số của khai triển, mỗi số hạng chỉ là ±1, tích nhiều sin", "tách 1/(k(k+1)) = 1/k − 1/(k+1); tổng hệ số thì thay x bằng một giá trị đặc biệt; tích sin / cos thì nhân thêm để dùng công thức góc nhân đôi", ["2023-S1-5", "2023-S1-8", "2026-SJ-5", "2026-SA-7"]),
],
"1.2": [
 ("a + 1/a, biểu thức đối xứng và Vieta", "a^2 + 3a + 1 = 0 hỏi biểu thức chứa a và 1/a; m + n và mn biết trước, tính m^5 + n^5", "chia cho a để được a + 1/a, rồi bình phương lên dần; biến đổi về tổng và tích, dùng định lý Vieta", ["2022-SJ-4", "2022-SA-3", "2023-S1-13", "2026-SJ-12", "2026-SA-6", "2023-S1-14"]),
 ("Hệ phương trình và phương trình chứa ẩn ở mẫu", "hệ có nghiệm chung, phương trình phân thức có nghiệm ngoại lai, phân tích đa thức hai biến", "giải phần không chứa tham số trước; quy đồng rồi nhớ loại nghiệm làm mẫu bằng 0; dùng biệt thức để có nghiệm", ["2022-SJ-6", "2022-SA-7", "2023-S1-6", "2023-S1-10", "2025-SJ-2", "2022-SA-8"]),
 ("Hàm số: hàm lẻ, phương trình hàm tuần hoàn", "f(x) + f(−x) là hằng số, f(x + 1) cho theo f(x), hỏi f(2026)", "ghép f(x) với f(−x); lặp công thức vài lần để tìm chu kỳ (thường 2, 4 hay 6) rồi chia 2026 cho chu kỳ", ["2022-SJ-2", "2026-SA-1"]),
],
"1.3": [
 ("Bình phương không âm, hoàn thành bình phương", "giá trị nhỏ nhất của biểu thức bậc hai hai biến, tổng các bình phương bằng 0", "viết thành tổng các bình phương cộng hằng số; tổng bình phương bằng 0 thì mỗi bình phương bằng 0", ["2023-S1-9", "2025-SJ-6", "2026-SJ-9", "2022-SA-2", "2022-SJ-12"]),
 ("Tổng các giá trị tuyệt đối", "tìm giá trị nhỏ nhất của |x − a1| + |x − a2| + …", "giá trị nhỏ nhất đạt tại trung vị của các điểm (đếm theo trọng số)", ["2022-SJ-7", "2025-SJ-7"]),
 ("AM-GM, tính đơn điệu, ràng buộc", "biến dương, tích không đổi, hàm có căn, nghiệm không âm", "AM-GM: tổng các số dương có tích không đổi nhỏ nhất khi các số bằng nhau; đặt ẩn phụ rồi xét miền giá trị của ẩn phụ", ["2026-SA-2", "2022-SA-10", "2025-SJ-3", "2026-SJ-14"]),
],
"2.1": [
 ("Phân tích nhân tử để ra số nguyên tố", "đa thức theo n là số nguyên tố, p^2 − k^2 = 4q^4", "phân tích thành tích; tích là số nguyên tố thì mọi thừa số trừ một phải là ±1; hiệu hai bình phương (p − k)(p + k)", ["2022-SA-5", "2023-S1-15", "2022-SJ-8", "2023-S1-17"]),
 ("Phương trình nghiệm nguyên", "ghép hai số thành số chính phương, hai biểu thức chia hết cho nhau, phương trình mũ 2^x − 1 = …", "đưa về tích bằng hằng số rồi liệt kê ước; đặt thương bằng ẩn mới rồi chặn; xét số dư theo mô-đun phù hợp", ["2022-SJ-10", "2026-SJ-7", "2026-SJ-11", "2026-SA-12"]),
 ("Hệ số nhị thức và tính chia hết", "chứng minh C(2p, p) − 2 chia hết cho p^2", "khai triển C(2p, p) = Σ C(p, k)^2; các số hạng giữa đều chia hết cho p", ["2026-SA-13"]),
],
"2.2": [
 ("Số dư, ƯCLN và chữ số tận cùng", "các số chia cho n có cùng số dư, ước chung lớn nhất cho trước, chữ số tận cùng của tích lớn", "cùng số dư thì n chia hết các hiệu; chữ số tận cùng chỉ cần nhân các chữ số tận cùng (có thừa số 5 và số lẻ thì tận cùng 5)", ["2023-S1-2", "2023-S1-4", "2025-SJ-5", "2025-SJ-10", "2026-SA-5"]),
 ("Phần nguyên và phần lẻ", "[x] và {x}, tổng nhiều số hạng [a + k/50]", "x = [x] + {x} với 0 ≤ {x} < 1; đếm xem có bao nhiêu số hạng vượt qua một số nguyên để chặn a", ["2025-SJ-12", "2026-SJ-6"]),
],
"3.1": [
 ("Song song, phân giác và tổng các góc", "đường song song, hai đường phân giác cắt nhau, hình răng cưa, tứ giác lõm", "góc so le, đồng vị; góc ngoài tam giác bằng tổng hai góc trong không kề; tứ giác lõm: góc lõm = tổng ba góc còn lại", ["2022-SJ-3", "2022-SJ-5", "2023-S1-3", "2025-SJ-4", "2026-SJ-2"]),
 ("Góc trong đa giác và trực tâm", "góc trong của đa giác lồi, trung điểm và đường cao trong tam giác", "tổng các góc trong của n-giác là (n − 2) × 180°, mỗi góc nhỏ hơn 180°; dùng đường trung bình song song với cạnh", ["2025-SJ-9", "2022-SA-9"]),
],
"3.2": [
 ("Pythagore, tam giác đặc biệt, gấp hình", "tam giác vuông cân, tam giác 30-60-90, gấp hình vuông, góc gấp đôi góc", "kẻ đường cao để tạo tam giác vuông đặc biệt; gấp hình thì hai phần trùng nhau bằng nhau; kéo dài cạnh để tạo tam giác cân", ["2023-S1-7", "2023-S1-16", "2026-SJ-4", "2026-SJ-8", "2026-SA-4"]),
 ("Tam giác đồng dạng và tứ giác nội tiếp", "chân các đường cao, tâm đường tròn nội tiếp, tam giác cân có đường tròn", "bốn điểm cùng nằm trên một đường tròn cho các góc bằng nhau, suy ra tam giác đồng dạng; định lý Ptolemy cho tứ giác nội tiếp", ["2026-SJ-10", "2026-SA-8", "2026-SA-10", "2022-SA-12"]),
 ("Diện tích và tọa độ", "các đường song song trong hình vuông, hình vuông nội tiếp tam giác vuông, parabol", "đổi tam giác lấy tam giác cùng đáy cùng chiều cao giữa hai đường song song; đặt tọa độ khi hình có góc vuông", ["2025-SJ-8", "2022-SA-6", "2022-SA-13"]),
],
"4.1": [
 ("Đếm: tổ hợp, đường đi, điểm nguyên", "đếm tam giác không chồng nhau, cách xếp đối xứng, diễn biến tỉ số trận đấu, số điểm nguyên trong elip", "chọn tổ hợp C(n, k); diễn biến tỉ số là đường đi trên lưới; chia trường hợp theo số phần tử được chọn", ["2022-SJ-9", "2022-SA-11", "2025-SJ-11", "2026-SJ-13", "2026-SA-11"]),
 ("Cực trị rời rạc và sắp xếp", "tập lớn nhất có tính chất, xếp số quanh vòng tròn, giá trị trên các đỉnh hình lập phương", "tìm một ví dụ đạt, rồi chứng minh chặn bằng đánh giá (tích ba số liên tiếp, thứ tự các giá trị)", ["2022-SJ-13", "2025-SJ-13", "2026-SA-9", "2026-SJ-15"]),
 ("Trò chơi và logic", "hai người lần lượt chọn số, người nói thật – nói dối trên bảng ô vuông", "người đi sau giữ một bất biến (tổng theo mô-đun); với nói thật – nói dối thì xét người chắc chắn nói dối trước rồi chia trường hợp", ["2022-SJ-11", "2023-S1-11"]),
],
}
