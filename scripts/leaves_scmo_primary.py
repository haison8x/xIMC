# Technique leaves for the SCMO primary mind map: sub-group -> [(title, sign, key, [example problem ids])].
# Few, broad leaves on purpose, so that every leaf collects several problems.
GROUP_VN = {
 1: ("Tính toán & số", "Calculation & Numbers"),
 2: ("Quy luật & đại lượng ẩn", "Patterns & Unknowns"),
 3: ("Toán có lời văn", "Word Problems"),
 4: ("Hình học & không gian", "Geometry & Spatial"),
 5: ("Đếm & logic", "Counting & Logic"),
}
SUB_VN = {
 "1.1": "Tính nhanh, thứ tự phép tính, điền dấu & ngoặc, tổng phân số", "1.2": "Chia hết, số nguyên tố, ước & số dư",
 "1.3": "Chữ số, phép tính chữ & số đối xứng",
 "2.1": "Dãy số, quy luật hình & tuần hoàn", "2.2": "Hình thay số, phép toán mới & tính ngược",
 "3.1": "Tổng – hiệu, chuyển bớt, tuổi, giả thiết tạm, thừa – thiếu",
 "3.2": "Tỉ số, phân số, phần trăm, trung bình, năng suất & nồng độ",
 "3.3": "Chuyển động: gặp nhau, đuổi kịp, tàu & thuyền", "3.4": "Thời gian, lịch, số khoảng, vị trí & đo lường",
 "4.1": "Chu vi", "4.2": "Diện tích", "4.3": "Đếm hình & góc", "4.4": "Khối lập phương, khai triển, gấp, lát hình & que diêm",
 "5.1": "Phương pháp đếm & Dirichlet", "5.2": "Suy luận: nói thật – nói dối, xếp hạng, cân",
 "5.3": "Câu đố lưới, điền số, trò chơi & tối ưu",
}
L = {
"1.1": [
 ("Thứ tự phép tính, điền dấu và đặt ngoặc", "biểu thức có cả + − × ÷ (hay có số 0), điền + / − hoặc ngoặc vào để được kết quả cho trước", "nhân chia trước, cộng trừ sau; điền dấu thì tính tổng tất cả rồi xem phải đổi dấu những số nào (mỗi số đổi dấu làm tổng giảm 2 lần số đó)", ["2020-P4-1", "2021-P3-1", "2023-MP-1", "2024-P2P3-1", "2025-P2P3-1", "2026-P3-1", "2026-P4-1", "2016-P3-9", "2023-P1P2-7", "2023-LP-3", "2026-P2-7", "2026-P3-2"]),
 ("Tính nhanh: ghép tròn, đặt thừa số chung, triệt tiêu", "các số gần tròn chục / tròn trăm, cùng một thừa số lặp lại, chuỗi × k ÷ k, số thập phân 2.5, 0.25", "ghép các số có tổng tròn; đặt thừa số chung ra ngoài; ×k rồi ÷k thì bỏ đi; 1 + 2 + … + n + … + 2 + 1 = n × n", ["2016-P3-1", "2020-P3-1", "2025-P4P5-1", "2023-P5-1", "2024-P4P5-1", "2024-P2P3-8", "2026-P6-1", "2023-UP-1", "2023-P4-1"]),
 ("Tổng phân số: tách hiệu, cấp số nhân, ước lượng, phần nguyên", "tổng nhiều phân số có mẫu là tích hai số liền nhau, mẫu là lũy thừa của 4, tổng nghịch đảo, tổng có làm tròn lên", "1/(n(n+1)) = 1/n − 1/(n+1) rồi rút gọn dây chuyền; cấp số nhân thì nhân tổng với công bội rồi trừ; ước lượng bằng chặn trên chặn dưới; phần nguyên thì gom các số hạng có cùng giá trị", ["2023-P6-10", "2024-P6-8", "2024-P6-13", "2026-P5-1", "2026-P6-9"]),
],
"1.2": [
 ("Bội, dấu hiệu chia hết, đếm bội", "số chia hết cho 105, 33, 9; đếm bội trong một khoảng; tổng trừ đi các bội của 6", "tách số chia thành tích các số nguyên tố cùng nhau rồi xét từng dấu hiệu (3, 9: tổng chữ số; 11: hiệu hàng lẻ – hàng chẵn); số bội = phần nguyên của n : k", ["2019-P3-3", "2023-P4-11", "2023-P5-12", "2023-P5-19", "2023-P6-2", "2024-P6-12", "2023-UP-7", "2024-P4P5-3"]),
 ("Số dư", "chia cho nhiều số có số dư cho trước, tổng các số dư, số dư khi chia cho 9, số dư lặp lại sau nhiều bước", "số dư bằng số chia trừ 1 thì số đó + 1 là bội chung (BCNN); dư khi chia cho 9 = dư của tổng chữ số; theo dõi số dư theo chu kỳ", ["2023-P5-14", "2023-P6-11", "2026-P5-7", "2026-P5-15", "2026-P6-14", "2026-P2-2"]),
 ("Số nguyên tố, phân tích thừa số, số ước và tổng ước", "các cạnh là số nguyên tố, phương trình với số nguyên tố, đếm thừa số 3 trong 2024!, số có đúng 12 ước", "chỉ có một số nguyên tố chẵn là 2 (xét chẵn lẻ); n = p^a × q^b có (a+1)(b+1) ước; đếm thừa số p trong n! bằng n : p + n : p^2 + …", ["2023-P6-9", "2024-P6-5", "2024-P6-15", "2024-P6-18", "2026-P4-13", "2026-P5-13", "2026-P6-16"]),
],
"1.3": [
 ("Phép cộng, trừ chữ", "phép cộng / trừ đặt cột, chữ cái hay chữ Hán hay hình vẽ thay chữ số, chữ số bị che", "chữ số đầu của tổng có thêm một hàng thì bằng 1; xét từng cột từ hàng đơn vị với số nhớ; muốn lớn nhất thì cho chữ số hàng cao lớn nhất trước", ["2016-P3-6", "2019-P3-4", "2020-P3-7", "2023-P3-12", "2023-MP-6", "2024-P2P3-12", "2024-P2P3-17", "2025-P2P3-12", "2025-P4P5-6", "2026-P1-3", "2026-P3-9"]),
 ("Phép nhân, chia chữ", "phép nhân hay phép chia dài có nhiều chữ số bị che, chữ số chỉ là số nguyên tố hay chỉ dùng 1–7", "bắt đầu từ chữ số tận cùng (tích các chữ số hàng đơn vị); dùng giới hạn độ dài của các tích riêng để chặn chữ số; thử ít trường hợp còn lại", ["2023-P5-13", "2023-P6-18", "2023-UP-5", "2024-P6-17", "2026-P4-16", "2026-P5-14", "2026-P6-7", "2025-P2P3-19"]),
 ("Giá trị theo hàng và hoán vị chữ số", "chục và đơn vị, nhóm theo 3, chuyển chữ số đầu xuống cuối, tổng / trung bình các số lập từ cùng các chữ số", "viết số thành 1000a + 100b + 10c + d rồi lập phương trình; các hoán vị: mỗi chữ số đứng ở mỗi hàng số lần như nhau, nên tổng = 111…1 × tổng chữ số × số lần", ["2023-P1P2-5", "2020-P3-3", "2023-P4-15", "2024-P6-9", "2023-P5-18", "2024-P4P5-15", "2026-P6-4", "2023-LP-6", "2020-P4-7"]),
 ("Số đối xứng và đếm chữ số", "số đọc xuôi ngược như nhau, cộng số với số viết ngược, đếm chữ số dùng để đánh số trang", "số đối xứng 4 chữ số do 2 chữ số đầu quyết định; ab + ba = 11(a + b); đếm chữ số theo nhóm 1, 2, 3 chữ số", ["2021-P3-8", "2024-P2P3-10", "2025-P2P3-8", "2026-P3-18", "2023-P5-3"]),
],
"2.1": [
 ("Dãy cách đều, số tam giác, hình lớn dần", "dãy tăng đều, đếm số hạng, tổng dãy, số khối lập phương / que diêm của hình thứ n", "số số hạng = (cuối − đầu) : khoảng cách + 1; tổng = số giữa × số số hạng; hình lớn dần thì lập công thức theo số thứ tự (1, 3, 6, 10 … rồi 1, 4, 10, 20 …)", ["2023-P1P2-4", "2023-P5-2", "2025-P4P5-5", "2023-P1P2-8", "2026-P1-10", "2026-P2-9", "2024-P4P5-11", "2020-P4-4"]),
 ("Dãy tuần hoàn", "hình hay số lặp lại theo nhóm, hỏi phần tử thứ 2016, chữ số tận cùng của tích, số dư của dãy Fibonacci", "tìm chu kỳ (có khi chỉ bắt đầu từ vài số hạng đầu), rồi lấy thứ tự chia cho độ dài chu kỳ, xem số dư", ["2023-P4-9", "2023-P6-8", "2024-P6-19", "2025-P2P3-15", "2026-P3-19", "2023-P1P2-3", "2026-P1-2", "2026-P2-8", "2021-P3-5"]),
 ("Quy luật trong bảng số và nhóm chữ", "hai dãy xen kẽ, bảng số nhiều hàng, 111…1 bình phương, hình xoay trong lưới, chuỗi chữ ghép từ hai mẫu", "tách vị trí lẻ / chẵn thành hai dãy; tìm công thức theo hàng và cột; với các mẫu chữ thì đếm số chữ mỗi loại và lập hệ phương trình", ["2023-P1P2-13", "2023-UP-14", "2024-P2P3-5", "2026-P2-4", "2025-P2P3-9", "2026-P4-17", "2026-P5-12"]),
],
"2.2": [
 ("Hình thay số: cùng hình là cùng số", "các phép tính với hình vuông, tam giác, quả bóng, con thỏ … thay cho số", "tìm hình chỉ xuất hiện trong một phép tính trước; gom nhóm hình giống nhau; so sánh hai dòng chỉ khác nhau một hình", ["2023-P1P2-1", "2024-P2P3-2", "2025-P2P3-2", "2026-P1-1", "2026-P2-1", "2023-LP-1"]),
 ("Phép toán mới và quan hệ giữa các đại lượng", "a ※ b = …, \"A gấp 5 lần B thêm 1\"", "thay số đúng theo định nghĩa; với quan hệ nhiều đại lượng thì biểu diễn tất cả theo một đại lượng rồi lập phương trình", ["2023-P3-17", "2023-P6-1", "2019-P3-7", "2020-P3-6"]),
 ("Tính ngược từ cuối", "biết kết quả sau nhiều bước (nhân đôi, bớt, quy tắc Collatz), hỏi số ban đầu", "đi ngược từng bước với phép tính ngược (nhân ↔ chia, cộng ↔ trừ); nếu một bước có hai khả năng ngược thì lập cây", ["2021-P3-4", "2023-P4-8", "2024-P2P3-18"]),
],
"3.1": [
 ("Tổng – hiệu, chuyển bớt, cân bằng nhóm", "biết tổng và hiệu, cho đi bao nhiêu để bằng nhau, đổi thẻ để các nhóm có tổng bằng nhau", "số lớn = (tổng + hiệu) : 2; chuyển một nửa hiệu thì bằng nhau; mỗi nhóm phải bằng tổng : số nhóm, rồi xem nhóm nào thừa / thiếu bao nhiêu", ["2016-P3-5", "2020-P4-5", "2023-P1P2-15", "2023-P1P2-16", "2023-P3-1", "2024-P2P3-4", "2026-P1-9", "2026-P2-10", "2026-P2-6", "2025-P2P3-14", "2026-P3-6", "2024-P2P3-13", "2024-P4P5-9", "2023-MP-10"]),
 ("Bài toán tuổi", "tổng tuổi, tuổi gấp mấy lần sau / trước vài năm", "hiệu tuổi không đổi; vẽ sơ đồ đoạn thẳng tại thời điểm có quan hệ gấp lần; tổng tuổi tăng thêm số người × số năm", ["2023-P3-6", "2024-P4P5-5", "2026-P3-15", "2026-P4-3"]),
 ("Giả thiết tạm: gà – thỏ, thưởng – phạt", "hai loại đối tượng với số chân / giá / điểm khác nhau, biết tổng số lượng và tổng chân / tiền / điểm", "giả sử tất cả là một loại, tính phần chênh lệch, chia cho chênh lệch của mỗi đối tượng; thưởng phạt thì mỗi lần sai mất cả phần thưởng lẫn phần phạt", ["2016-P3-3", "2016-P3-11", "2020-P3-8", "2023-P3-10", "2023-P4-2", "2023-MP-5", "2024-P2P3-9", "2025-P2P3-4", "2026-P4-8", "2025-P2P3-10", "2025-P2P3-16", "2025-P4P5-9"]),
 ("Thừa – thiếu", "chia mỗi người a thì thừa, mỗi người b thì thiếu", "số người = (thừa + thiếu) : (b − a); cả hai lần đều thừa (hay đều thiếu) thì lấy hiệu", ["2023-P4-18", "2026-P3-3", "2026-P4-2"]),
],
"3.2": [
 ("Tỉ số, phân số của một số, tỉ số thay đổi", "chia theo tỉ số, A bằng 2/3 của B, thêm / bớt một loại làm tỉ số đổi", "giữ cố định đại lượng không đổi và quy đồng số phần của nó qua các bước; một phần = số đã biết : số phần tương ứng", ["2023-P4-4", "2023-P5-10", "2023-P6-3", "2023-UP-6", "2024-P4P5-2", "2024-P4P5-13", "2024-P6-6", "2026-P3-10", "2024-P6-3"]),
 ("Trung bình cộng", "điểm trung bình thay đổi khi thêm / bớt người, các nhóm trùng nhau", "làm việc với tổng (tổng = trung bình × số lượng) rồi trừ hai tổng; phần chênh lệch so với trung bình phải bù trừ nhau", ["2023-P4-3", "2024-P4P5-6", "2025-P2P3-6", "2026-P4-7", "2026-P5-5"]),
 ("Năng suất và công việc", "làm trong 8 phút được bao nhiêu, hai người cùng làm, chia tiền công theo phần việc", "tính phần việc làm được trong 1 đơn vị thời gian; thay một người bằng người kia theo tỉ số năng suất; chia tiền theo tỉ số phần việc", ["2016-P3-2", "2023-P5-6", "2024-P4P5-18", "2026-P4-12"]),
 ("Phần trăm, giá bán và nồng độ", "giảm giá, lãi phần trăm, rau quả khô nước, pha dung dịch", "giữ cố định phần không đổi (giá vốn, chất khô, chất tan); pha trộn thì dùng sơ đồ chéo: lượng tỉ lệ nghịch với khoảng cách đến nồng độ cần pha", ["2023-P5-9", "2023-P6-6", "2023-UP-3", "2026-P5-16", "2026-P6-11"]),
],
"3.3": [
 ("Gặp nhau, đuổi kịp, đường vòng", "hai người đi ngược / cùng chiều, xuất phát lệch giờ, chạy vòng hồ, gặp nhau lần hai", "gặp nhau: tổng vận tốc; đuổi kịp: hiệu vận tốc; đến lần gặp thứ hai thì tổng quãng đường gấp 3 lần thứ nhất; dùng tỉ số vận tốc khi cùng thời gian", ["2023-P4-14", "2023-P6-15", "2023-UP-10", "2024-P6-2", "2024-P6-11", "2026-P4-4", "2026-P5-11", "2026-P6-13"]),
 ("Tàu qua cầu, qua hầm, thuyền trên sông", "đoàn tàu đi qua cầu / hầm, thuyền xuôi và ngược dòng, vật rơi xuống sông", "tàu qua cầu đi quãng đường = dài cầu + dài tàu; xuôi = thuyền + nước, ngược = thuyền − nước; vật trôi thì vận tốc dòng nước triệt tiêu", ["2023-P5-11", "2024-P4P5-7", "2023-P5-17", "2023-P6-17"]),
 ("Tỉ số vận tốc – thời gian, vận tốc trung bình", "đi nhanh hơn thì đến sớm hơn bao nhiêu, đi và về với vận tốc khác nhau", "cùng quãng đường thì thời gian tỉ lệ nghịch với vận tốc; vận tốc trung bình = tổng quãng đường : tổng thời gian (tự chọn quãng đường cho dễ chia)", ["2019-P3-5", "2024-P4P5-8", "2026-P5-6", "2026-P6-5"]),
],
"3.4": [
 ("Lịch và thứ trong tuần", "ngày này là thứ mấy, năm nào 1/1 lại rơi vào thứ Tư, sau bao nhiêu tháng / năm", "đếm số ngày rồi chia cho 7 lấy số dư; năm thường lùi 1 thứ, năm nhuận lùi 2 thứ; tháng có 31 ngày thì có 3 thứ xuất hiện 5 lần", ["2016-P3-7", "2023-P3-5", "2025-P4P5-2", "2026-P4-11", "2026-P6-3", "2026-P3-5", "2019-P3-1", "2023-MP-3"]),
 ("Số khoảng: cưa gỗ, leo tầng, bước chân, gấp dây", "cưa thành mấy đoạn, leo từ tầng 1 lên tầng 4, gấp đôi dây nhiều lần rồi cắt", "số khoảng = số điểm − 1 (cưa n đoạn chỉ cần n − 1 nhát; lên tầng n chỉ leo n − 1 tầng); gấp đôi k lần thì dây thành 2^k lớp", ["2023-P1P2-11", "2023-P3-4", "2026-P1-7", "2025-P2P3-11"]),
 ("Vị trí trong hàng, đi tới đi lui, mô phỏng thời gian", "đứng thứ mấy từ đầu và từ cuối, đi quá rồi quay lại, đèn giao thông đổi màu", "tổng số = thứ tự từ đầu + thứ tự từ cuối − 1; vẽ trục thẳng để cộng các đoạn đi quá; mô phỏng từng phút khi có chu kỳ", ["2023-P3-3", "2024-P2P3-14", "2023-P1P2-9", "2023-P3-2", "2023-LP-11"]),
],
"4.1": [
 ("Dời cạnh: hình bậc thang, chữ L, cầu thang", "hình có nhiều góc vuông, cầu thang trải thảm, các mảnh chữ L ghép lại", "dời các cạnh ngang lên trên, cạnh dọc sang bên để thành hình chữ nhật; chỉ cộng thêm những đoạn không dời được", ["2023-P3-11", "2023-P4-16", "2023-P4-10", "2025-P2P3-13", "2025-P4P5-3", "2023-MP-4", "2019-P3-6"]),
 ("Ghép và bớt hình vuông: chu vi đổi bao nhiêu", "ghép các hình vuông, bỏ bớt ô vuông, hình gồm các ô vuông đơn vị", "chu vi = tổng chu vi các mảnh − 2 × tổng độ dài cạnh chung; bớt một ô có khi làm chu vi tăng", ["2024-P2P3-6", "2026-P2-11", "2026-P3-12", "2026-P4-5", "2020-P4-6", "2025-P2P3-7"]),
 ("Chu vi và diện tích, rào vườn", "hình chữ nhật và hình vuông có cùng chu vi, rào vườn có một cạnh dựa vào tường", "nửa chu vi = dài + rộng; cạnh dựa tường không cần rào, nên chọn cạnh dài nhất dựa tường", ["2023-P3-16", "2026-P3-8"]),
],
"4.2": [
 ("Mô hình nửa diện tích, chung đáy chung cao", "tam giác có đỉnh trên cạnh hình chữ nhật, điểm bất kỳ bên trong, hai hình chung một tam giác", "tam giác chung đáy và chiều cao với hình chữ nhật thì bằng nửa hình chữ nhật; điểm bất kỳ thì dời về đỉnh cho dễ tính", ["2023-P4-7", "2023-P5-16", "2024-P4P5-4", "2026-P4-10", "2026-P5-8", "2025-P4P5-7", "2024-P4P5-19", "2023-P5-5", "2020-P3-5"]),
 ("Tỉ số diện tích: cánh bướm, đuôi én, chia cạnh", "hình thang có hai đường chéo, cạnh chia ba phần, lục giác đều, hình chữ nhật chia thành nhiều phần", "hai tam giác chung chiều cao thì tỉ số diện tích bằng tỉ số đáy; mô hình cánh bướm trong hình thang: tích hai tam giác bên bằng tích hai tam giác trên dưới", ["2023-P6-7", "2023-P4-12", "2023-UP-13", "2024-P6-4", "2026-P5-19", "2020-P4-8", "2026-P6-18", "2024-P6-7", "2026-P6-12"]),
 ("Hình tròn và hình quạt: cắt ghép", "nửa hình tròn trong hình vuông, phần tư hình tròn, các hình quạt quanh hình thoi", "cắt rồi dời các phần cong để ghép thành hình quen thuộc; tổng các góc ở tâm là 360° thì ghép thành một hình tròn", ["2023-P6-4", "2023-UP-2", "2024-P6-10", "2026-P6-8"]),
 ("Cạnh hình vuông, đối xứng, diện tích lớn nhất", "hai hình vuông cạnh nhau biết tổng / hiệu cạnh, hình vuông chồng nhau đối xứng, chu vi cố định thì diện tích lớn nhất", "tính cạnh bằng tổng – hiệu; dùng đối xứng để gộp các mảnh; cùng chu vi thì hình vuông có diện tích lớn nhất", ["2023-P4-5", "2023-P6-16", "2024-P2P3-16", "2024-P4P5-16", "2024-P4P5-14", "2026-P4-14", "2026-P5-9"]),
],
"4.3": [
 ("Đếm hình tam giác", "hình có nhiều đoạn thẳng cắt nhau, đếm có tất cả bao nhiêu tam giác", "đếm theo số mảnh nhỏ ghép thành (1 mảnh, 2 mảnh, …) hoặc theo đỉnh; từ một đỉnh kẻ n đường xuống đáy thì có 1 + 2 + … + n tam giác", ["2019-P3-2", "2023-MP-2", "2024-P2P3-3", "2026-P4-6", "2026-P5-4", "2026-P6-6", "2023-P1P2-2"]),
 ("Đếm hình vuông, hình chữ nhật", "lưới ô vuông, dãy ô liền nhau, hình chứa một ô cho trước", "lưới n × n có 1^2 + 2^2 + … + n^2 hình vuông; số hình chữ nhật = chọn 2 đường dọc × chọn 2 đường ngang; một dãy n ô có 1 + 2 + … + n đoạn", ["2016-P3-4", "2020-P3-2", "2020-P4-3", "2023-P5-8", "2025-P2P3-3", "2025-P4P5-4", "2026-P2-5", "2026-P3-7", "2021-P3-3", "2026-P1-6"]),
 ("Góc", "đếm góc, tam giác bị gấp, ngũ giác đều với tam giác đều, góc ngoài", "tổng góc tam giác 180°, tứ giác 360°, góc ngoài bằng tổng hai góc trong không kề; tìm tam giác cân để tính góc đáy", ["2023-P3-8", "2023-P5-7", "2024-P4P5-10", "2026-P5-2", "2026-P6-2"]),
],
"4.4": [
 ("Khối lập phương: sơn mặt, diện tích bề mặt, xúc xắc", "khối xếp từ nhiều hình lập phương, đếm mặt được sơn, diện tích bề mặt, mặt đối diện của xúc xắc", "đếm mặt nhìn thấy theo 6 hướng (trên, dưới, trước, sau, trái, phải); mặt đối diện của xúc xắc có tổng 7", ["2023-P1P2-18", "2026-P3-14", "2024-P6-1", "2023-P6-19", "2024-P2P3-7"]),
 ("Hình khai triển, gấp, xoay và đối xứng", "hình khai triển của hình lập phương, gấp giấy, xoay 180°, cắt một góc hình vuông", "tưởng tượng gấp lại: các mặt cách một ô trên một hàng là mặt đối diện; xoay 180° thì 6 ↔ 9 và 0, 1, 2, 5, 8 giữ nguyên", ["2023-P5-4", "2023-LP-9", "2026-P6-15", "2023-LP-10", "2023-UP-4", "2023-P1P2-10"]),
 ("Cắt ghép, lát hình, que diêm", "chia hình thành các mảnh giống nhau, lát cầu thang bằng hình vuông, đếm que diêm trong lưới", "đếm que theo hàng ngang và hàng dọc riêng; lát hình thì xét ô góc khó nhất trước rồi chia trường hợp", ["2016-P3-8", "2023-P1P2-12", "2020-P4-11", "2021-P3-7", "2021-P3-9", "2026-P1-4"]),
],
"5.1": [
 ("Quy tắc nhân, quy tắc cộng, chia trường hợp", "đếm số có điều kiện chữ số, xếp người có hạn chế vị trí, bắt tay, chọn cặp, chia kẹo", "đặt đối tượng bị hạn chế trước; chia trường hợp rồi cộng; đếm phần bù (tổng − không thỏa mãn); chia đồ giống nhau dùng phương pháp vách ngăn", ["2023-P6-12", "2023-P5-15", "2024-P4P5-12", "2026-P2-3", "2026-P1-5", "2020-P3-9", "2021-P3-2", "2023-P6-5", "2024-P4P5-17", "2020-P4-2", "2026-P6-19", "2026-P6-17", "2024-P6-16"]),
 ("Sơ đồ cây và đếm đường đi", "các kết quả trận đấu, chuyền bóng, đường đi chỉ sang phải / lên trên, thứ tự lấy gạch", "vẽ sơ đồ cây khi số bước nhỏ; đường đi trên lưới thì ghi số cách đến mỗi ô = tổng số cách của các ô đi tới nó", ["2023-P4-13", "2024-P2P3-11", "2023-P4-17", "2026-P4-15", "2023-P3-9", "2026-P3-13"]),
 ("Tô màu và xếp có điều kiện", "tô màu các ô kề nhau khác màu, xếp số quanh vòng tròn, điền số 0 không kề nhau", "tô / điền ô có nhiều ràng buộc nhất trước; với lưới dài thì tìm số cách cho một cột rồi nhân dần", ["2023-UP-11", "2026-P5-18", "2023-MP-9", "2025-P4P5-11"]),
 ("Nguyên lý Dirichlet và trường hợp xấu nhất", "phải lấy ít nhất bao nhiêu để chắc chắn có …", "giả sử xấu nhất: lấy hết các loại không mong muốn trước, rồi cộng thêm 1", ["2023-P6-14", "2024-P6-14", "2026-P3-4", "2026-P4-9", "2026-P2-13"]),
],
"5.2": [
 ("Người nói thật – người nói dối", "mỗi người nói một câu, biết ai luôn nói thật, ai luôn nói dối", "giả sử một người nói thật rồi suy ra tiếp đến khi gặp mâu thuẫn; hai câu nói trái ngược nhau thì đúng một người nói thật", ["2020-P3-10", "2023-P3-18", "2023-MP-7", "2024-P2P3-15", "2026-P1-11", "2026-P3-17", "2021-P3-11", "2025-P2P3-5"]),
 ("Xếp hạng, so sánh, cân thăng bằng", "ai nhanh hơn ai, thứ tự về đích, cân đĩa so sánh khối lượng, tìm đồng xu giả", "sắp các quan hệ \"lớn hơn\" thành một dãy; cân thì so sánh hai vế sau khi bỏ phần giống nhau; chia đồng xu thành 3 nhóm", ["2019-P3-9", "2023-P1P2-6", "2023-P1P2-14", "2023-P4-6", "2023-LP-5", "2023-LP-7", "2025-P2P3-18", "2026-P3-11", "2026-P5-3"]),
 ("Bảng suy luận, đoán và khớp", "nhiều người đoán, mỗi người đúng một số câu; hội thoại \"tôi không biết\"", "lập bảng hàng – cột rồi loại dần; tìm các câu mà hai người đoán giống nhau; mỗi câu \"không biết\" loại bỏ các khả năng sẽ cho biết ngay", ["2023-P4-19", "2023-UP-8", "2025-P4P5-8", "2026-P4-18", "2026-P5-17"]),
],
"5.3": [
 ("Hình vuông Latin, sudoku và câu đố lưới", "điền số sao cho mỗi hàng, mỗi cột có đủ các số, có thêm gợi ý ở cạnh lưới hay vùng đặc biệt", "bắt đầu ở hàng / cột / vùng còn ít ô trống nhất hoặc có gợi ý mạnh nhất; mỗi lần điền chỉ ghi số chắc chắn", ["2016-P3-10", "2020-P3-4", "2020-P4-10", "2021-P3-6", "2023-P1P2-19", "2023-LP-8", "2023-LP-12", "2024-P2P3-19", "2026-P4-19"]),
 ("Điền số vào hình", "điền số vào các vòng tròn, đường thẳng, ô lục giác để tổng bằng nhau hoặc thỏa điều kiện", "ô nằm trên nhiều đường được đếm nhiều lần: tổng các đường − tổng các số = phần đếm thừa; xét chẵn lẻ để định vị số đặc biệt", ["2023-P1P2-17", "2023-P3-13", "2023-P3-14", "2023-UP-9", "2026-P1-8", "2026-P3-16", "2019-P3-11", "2023-MP-11"]),
 ("Trò chơi, chiến lược và bất biến", "hai người lần lượt đi, đổi số theo quy tắc, số bước ít nhất để đạt mục tiêu", "đi ngược từ đích; tìm đại lượng không đổi (bất biến) sau mỗi bước; người đi sau thường bắt chước / đối xứng", ["2023-P3-7", "2023-P3-19", "2023-P6-13", "2020-P3-11", "2021-P3-10", "2023-MP-8"]),
 ("Tối ưu: đường đi, đổi quà, xếp cặp", "lớn nhất / nhỏ nhất có thể, đường đi qua tất cả cửa, đổi vỏ lấy quà, ghép cặp phân số", "thử trường hợp tốt nhất rồi chứng minh không thể tốt hơn; đường đi qua mọi cửa một lần thì bắt đầu và kết thúc ở phòng có số cửa lẻ", ["2019-P3-8", "2019-P3-10", "2020-P4-9", "2023-LP-2", "2023-LP-4", "2025-P2P3-17", "2025-P4P5-10", "2026-P2-12", "2026-P5-10", "2026-P6-10", "2023-P3-15"]),
],
}
