# Technique leaves for the ICO mind map: sub-group -> [(title, sign, key, [example problem ids])].
# Few, broad leaves on purpose, so that every leaf collects several problems.
GROUP_VN = {
 1: ("Đếm", "Counting"),
 2: ("Đồ thị", "Graphs"),
 3: ("Trò chơi & quá trình", "Games & Processes"),
 4: ("Cực trị & bất biến", "Extremal Principles & Invariants"),
 5: ("Bảng, tô màu & hình", "Tables, Colourings & Geometry"),
}
SUB_VN = {
 "1.1": "Quy tắc cộng, nhân, chia trường hợp, xác suất", "1.2": "Song ánh, đếm hai cách, truy hồi",
 "2.1": "Quen biết, bậc, giải đấu", "2.2": "Đường đi, cây, lưới",
 "3.1": "Trò chơi & chiến lược thắng", "3.2": "Thao tác lặp & thuật toán",
 "4.1": "Chặn rồi dựng ví dụ", "4.2": "Bất biến, đơn biến, chẵn lẻ", "4.3": "Nguyên lý Dirichlet",
 "5.1": "Bảng & tô màu", "5.2": "Lát hình & chia hình", "5.3": "Hình học tổ hợp",
}
L = {
"1.1": [
 ("Quy tắc nhân theo từng bước", "các lựa chọn độc lập nhau hoặc hình tách được thành các phần rời", "đếm số cách cho từng bước (từng phần) rồi nhân lại", ["2020-R1-6", "2021-R1-5", "2025-J-12"]),
 ("Xác suất bằng đếm trường hợp", "hỏi xác suất hoặc giá trị trung bình", "xác suất = số thuận lợi / tổng số; trung bình thì tách theo từng phần rồi cộng (tuyến tính)", ["2020-R2-2", "2024-R1-10", "2025-R2-7"]),
 ("Chia trường hợp theo vị trí đặc biệt", "có một phần tử, vị trí hay giá trị then chốt chi phối cả bài", "chia theo yếu tố then chốt, đếm riêng từng trường hợp rồi cộng", ["2021-R1-3", "2021-R1-11", "2024-R1-6", "2024-R1-11", "2025-J-5", "2025-J-6", "2025-J-10", "2025-I-13"]),
 ("Đếm phần bù", "điều kiện dạng \"mỗi ... đều có ít nhất một\"", "đếm tất cả rồi trừ trường hợp xấu, dùng bao hàm – loại trừ", ["2021-R1-9", "2025-I-5"]),
],
"1.2": [
 ("Song ánh sang đối tượng dễ đếm", "đối tượng khó đếm trực tiếp nhưng tương ứng 1–1 với đối tượng quen (đường đi, tập con, giá trị)", "dựng song ánh rồi đếm đối tượng mới", ["2020-R1-2", "2020-R1-14", "2021-R1-14", "2024-R1-3", "2025-J-2", "2025-I-9", "2025-I-12"]),
 ("Đếm hai cách", "một tổng hay số cặp có thể đếm theo hai góc nhìn", "đếm cùng một đại lượng theo hai cách rồi so sánh để ra đẳng thức hoặc bất đẳng thức", ["2020-R1-5", "2021-R2-1", "2024-R2-3"]),
 ("Truy hồi theo phần tử cuối", "đối tượng xây dựng dần theo độ dài n", "xét bước cuối cùng để lập công thức truy hồi", ["2020-R1-7", "2025-J-1", "2025-I-1", "2025-I-11"]),
],
"2.1": [
 ("Giải đấu: đếm thắng thua", "mỗi cặp đội gặp nhau đúng một lần", "tổng số trận cố định; so sánh số trận thắng, điểm giữa các đội", ["2020-R1-4", "2020-R2-1"]),
 ("Bậc của đỉnh và tổng bậc", "hỏi số cạnh, số tam giác, số quan hệ trong đồ thị", "tổng bậc = 2 × số cạnh; chặn qua bậc từng đỉnh rồi cộng lại", ["2024-R2-4", "2025-J-3", "2025-I-7"]),
],
"2.2": [
 ("Đường đi ngắn nhất trên lưới / đồ thị", "di chuyển giữa các ô, đỉnh; hỏi số bước tối thiểu hoặc cần nối các đỉnh bằng đường đi", "tính khoảng cách, xét đường đi ngắn nhất và vật cản", ["2020-R1-1", "2020-R1-15", "2025-J-14", "2025-I-4"]),
 ("Cây: số cạnh, đường kính", "đồ thị liên thông không chu trình, đường đi dài nhất", "cây n đỉnh có n−1 cạnh; xét đường kính và các nhánh treo vào nó", ["2020-R1-13", "2024-R1-13", "2024-R1-14", "2024-R1-15"]),
],
"3.1": [
 ("Xây chiến lược cho từng bên", "hai người chơi đều chơi tối ưu; hỏi ai thắng hoặc kết quả tốt nhất mà một bên chắc chắn đạt được", "Dựng chiến lược cho bên này để chặn một phía (ghép cặp, đối xứng, đáp trả từng nước), rồi dựng chiến lược cho bên kia để chặn phía còn lại; hai chặn bằng nhau là đáp số.", ["2024-R1-1", "2024-R1-4", "2025-R2-6"]),
 ("Vị trí thắng – thua (quy nạp lùi)", "Hai người chơi tối ưu, hỏi kết quả cuối cùng", "Tính kết quả cho trạng thái nhỏ (khoảng trống còn lại), quy nạp lùi: mỗi bên chọn nước tốt nhất, thường dẫn tới chia đôi", ["2025-J-11", "2025-I-6"]),
],
"3.2": [
 ("Hỏi – đáp, tìm kiếm chia đôi", "tìm một đối tượng bằng ít câu hỏi, phép thử nhất", "mỗi câu hỏi chia đôi tập khả năng; chặn dưới bằng lập luận đối thủ", ["2020-R2-7", "2021-R2-7"]),
 ("Mô phỏng vài bước để tìm quy luật", "quá trình lặp lại hoặc chuyển động theo luật cố định", "chạy thử vài bước, phát hiện chu kỳ hoặc tính đối xứng rồi chứng minh", ["2021-R2-3", "2024-R1-9"]),
],
"4.1": [
 ("Chặn trên rồi dựng ví dụ đạt", "hỏi giá trị lớn nhất hoặc nhỏ nhất", "chứng minh chặn (trên hoặc dưới) rồi dựng cấu hình đạt đúng giá trị đó", ["2020-R1-12", "2021-R1-2", "2021-R1-7", "2021-R1-8", "2021-R1-12", "2021-R1-15", "2021-R2-2", "2024-R1-12", "2024-R2-1", "2024-R2-2", "2024-R2-5", "2024-R2-6", "2025-J-4", "2025-J-7", "2025-J-13", "2025-I-2", "2025-I-8", "2025-R2-1", "2025-R2-4"]),
 ("Xét phần tử cực hạn", "cần chứng minh tồn tại hoặc dùng phản chứng", "xét phần tử lớn nhất, nhỏ nhất hoặc cấu hình tối thiểu rồi suy ra mâu thuẫn", ["2020-R2-5", "2021-R2-4", "2025-R2-3"]),
],
"4.2": [
 ("Bất biến và đơn biến", "một thao tác được lặp lại nhiều lần; hỏi trạng thái nào đạt được, hoặc quá trình có dừng không", "Tìm đại lượng không đổi sau mỗi bước (bất biến) để loại các trạng thái không thể đạt, hoặc đại lượng luôn tăng/giảm và bị chặn (đơn biến) để chứng minh quá trình phải dừng.", ["2020-R1-3", "2020-R1-11", "2024-R1-7", "2024-R1-8"]),
 ("Tô màu, chẵn lẻ để chặn", "lưới hoặc dãy có cấu trúc tuần hoàn, cần chứng minh không thể", "tô màu theo mod 2, mod 3 rồi xét chẵn lẻ, số dư để ra mâu thuẫn", ["2020-R2-6", "2025-J-8", "2025-J-15", "2025-I-3", "2025-I-10"]),
],
"4.3": [
 ("Dirichlet: chia ngăn hợp lý", "nhiều đối tượng, cần có hai cái cùng tính chất hoặc chặn kích thước một họ", "chia thành các ngăn sao cho mỗi ngăn chứa tối đa một phần tử hợp lệ rồi đếm", ["2020-R2-4", "2021-R1-13", "2021-R2-5"]),
],
"5.1": [
 ("Bảng: xét theo hàng, cột và quy luật tô", "bảng điền số hoặc tô màu với điều kiện trên từng hàng, cột hay ô kề nhau", "Xét riêng từng hàng và từng cột (tổng, số ô tô màu) rồi cộng lại, hoặc tìm quy luật tô lặp lại theo chu kỳ; điều kiện trên các ô kề nhau thường ép cả bảng theo một mẫu.", ["2020-R1-8", "2021-R1-6", "2021-R1-10", "2024-R1-5"]),
],
"5.2": [
 ("Chia bảng thành vùng", "đặt tối đa đối tượng trên bảng với ràng buộc cục bộ", "chia bảng thành khối nhỏ (2×2, ...), mỗi khối chứa tối đa vài đối tượng rồi cộng lại", ["2020-R1-9", "2021-R1-4", "2025-J-9", "2025-I-14", "2025-I-15", "2025-R2-2"]),
],
"5.3": [
 ("Dây cung và giao điểm", "điểm trên đường tròn hoặc đa giác lồi, các dây cung, cạnh cắt nhau", "một dây cung chia hình thành hai phía; quy nạp trên từng phía; đếm giao điểm", ["2020-R1-10", "2020-R2-3", "2021-R2-6"]),
 ("Điểm trong mặt phẳng, bao lồi", "điểm trên mặt phẳng, không ba điểm thẳng hàng", "xét bao lồi, điểm ngoài cùng (trái, phải, trên, dưới) và tam giác phân", ["2021-R1-1", "2024-R1-2", "2024-R2-7", "2025-R2-5"]),
],
}
