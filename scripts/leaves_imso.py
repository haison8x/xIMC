# Technique leaves for the IMSO mind map. IMSO uses the IMC Key Stage 2 sub-groups, so the
# leaves of leaves_ks2 are reused with IMSO example problems (a KS2 leaf with no IMSO example is
# left out), and IMSO-specific leaves are added after them.
from leaves_ks2 import GROUP_VN, L as KS2_L, SUB_VN  # noqa: F401  (GROUP_VN/SUB_VN used by build.py)
from leaves_util import merge_leaves

# KS2 leaf id -> IMSO example problems
EXAMPLES = {
 "1.1-a": ["2006-S20", "2009-Q1", "2022-S11"],
 "1.1-b": ["2009-S8", "2011-S9", "2012-S7", "2012-S8"],
 "1.1-d": ["2011-S22", "2011-E5", "2020-S3", "2025-S12", "2025-E4", "2009-E2"],
 "1.1-e": ["2005-S6", "2014-S18", "2018-S14", "2008-S11"],
 "1.1-f": ["2025-S2"],
 "1.1-h": ["2024-E11", "2018-S9", "2018-S23", "2021-S18", "2013-E7", "2019-S16"],
 "1.1-k": ["2010-S14", "2011-E10", "2005-E5"],
 "1.2-a": ["2011-S7", "2014-S17", "2020-S16", "2022-S25", "2021-E5", "2020-S10"],
 "1.2-b": ["2010-S25", "2012-S13", "2016-S19", "2015-X3", "2008-Q11", "2016-E7"],
 "1.2-c": ["2007-S9", "2010-S24", "2011-S1", "2017-S1", "2016-S11", "2021-S8", "2018-E3"],
 "1.2-d": ["2022-S18"],
 "1.2-e": ["2016-E2", "2020-E9", "2022-E12"],
 "1.3-a": ["2006-S1", "2012-S2", "2022-S6", "2019-S4"],
 "1.3-b": ["2008-S7", "2015-S8", "2015-S14"],
 "1.3-c": ["2024-S7", "2023-E7", "2015-S2", "2005-S3", "2014-X4"],
 "1.4-a": ["2010-S4", "2015-S1", "2012-S23", "2019-E7", "2025-E1"],
 "1.4-d": ["2011-S5"],
 "2.1-a": ["2008-S3", "2011-S12", "2013-S6", "2009-S4", "2012-S12", "2025-S14"],
 "2.1-b": ["2016-E12", "2013-S20", "2009-E8"],
 "2.1-c": ["2021-S22", "2018-E11", "2008-E6"],
 "2.2-a": ["2010-S15", "2019-S17", "2019-S20", "2018-S22", "2006-S23", "2009-S9", "2021-E4"],
 "2.2-b": ["2016-E3", "2015-S11", "2013-E3", "2009-Q6", "2012-E9"],
 "2.2-c": ["2008-Q6", "2016-X2", "2010-X5", "2018-X1", "2022-S19", "2017-S7"],
 "2.3-a": ["2007-S23", "2008-S9", "2015-S10", "2022-S22"],
 "2.3-b": ["2010-S19", "2023-E3", "2017-E8", "2018-S5", "2005-S17"],
 "2.4-a": ["2007-S5", "2014-S7", "2017-S10", "2016-S23", "2022-S15", "2017-S15", "2022-S8", "2014-E8"],
 "3.1-b": ["2014-S1"],
 "3.1-c": ["2007-S19", "2010-S13", "2011-S8", "2013-S2", "2013-S5", "2016-S17", "2017-S4", "2022-S24"],
 "3.2-a": ["2007-S1", "2011-S4", "2012-E1", "2005-S1", "2010-E9", "2023-S5", "2025-S8"],
 "3.2-b": ["2020-S5"],
 "3.2-d": ["2015-S24"],
 "3.3-a": ["2012-S1", "2010-S12", "2006-E2", "2014-S4", "2017-S9"],
 "3.3-c": ["2009-X2"],
 "3.4-a": ["2011-S2", "2012-S16", "2023-S2", "2023-S3", "2010-S11", "2007-S16", "2005-S12"],
 "3.4-b": ["2006-S9", "2012-E3", "2021-X4"],
 "3.5-a": ["2012-E5"],
 "3.5-b": ["2007-S7", "2009-S2", "2009-S7", "2006-S2", "2005-E2", "2021-S12"],
 "3.5-c": ["2010-E11", "2010-E12", "2007-E1"],
 "3.5-d": ["2014-S10", "2009-S3", "2014-S16"],
 "4.1-a": ["2019-S7"],
 "4.1-c": ["2006-E11"],
 "4.1-d": ["2008-Q8", "2015-S15", "2021-S4", "2021-S5", "2017-S16"],
 "4.2-a": ["2006-S8", "2007-E13", "2008-Q7", "2025-E6"],
 "4.2-b": ["2023-S17", "2009-E1"],
 "4.3-a": ["2018-S7", "2011-E9"],
 "4.3-c": ["2008-E3", "2008-S12"],
 "5.1-a": ["2010-S1", "2012-E11", "2023-S23", "2023-E8", "2025-E5", "2008-E8"],
 "5.1-b": ["2010-E1", "2013-E5", "2018-S2", "2020-S19", "2015-S19", "2022-E5"],
 "5.1-c": ["2011-E12", "2025-S9", "2022-E13", "2019-E8", "2020-E13", "2012-E12"],
 "5.1-d": ["2013-S11", "2021-S6", "2007-S24"],
 "5.1-e": ["2005-S5", "2007-E6", "2014-S9", "2017-S17", "2020-E7", "2017-E7"],
 "5.2-a": ["2005-S16", "2007-S18", "2011-S11", "2018-S16", "2022-S9", "2016-S16"],
 "5.2-b": ["2008-E4", "2017-E10", "2021-S14", "2021-S23", "2025-S13", "2007-E10"],
 "5.2-c": ["2008-S16", "2015-S4", "2020-S12", "2022-S23", "2013-S10"],
 "5.2-d": ["2006-S15", "2007-S15", "2012-S4", "2014-S25", "2021-E3", "2019-E1"],
 "5.3-a": ["2005-S13", "2007-E8", "2010-S3", "2011-S3", "2023-S7", "2010-E8", "2013-S7"],
 "5.3-b": ["2007-S12", "2010-S18", "2021-S11"],
 "5.3-c": ["2009-E9", "2022-S5"],
 "5.4-a": ["2018-S6", "2014-S6", "2019-S1", "2016-S3"],
 "5.4-d": ["2006-E3", "2014-E11", "2020-E10", "2020-X2", "2023-X6", "2016-X4", "2022-X2", "2025-X1"],
 "5.5-a": ["2005-S19", "2007-S8", "2006-S12", "2013-S21"],
 "5.5-b": ["2023-S1", "2013-X1"],
 "5.5-c": ["2010-E10", "2006-S21"],
 "5.5-d": ["2009-Q3", "2021-S3", "2019-E4", "2005-S4", "2016-S4"],
 "6.1-a": ["2023-E12"],
 "6.1-b": ["2024-S6", "2012-S10"],
 "6.1-d": ["2005-X2", "2006-S6"],
 "6.1-e": ["2015-S6", "2022-S16"],
 "6.2-a": ["2024-S21", "2006-S7", "2005-E6", "2015-S16", "2019-S25", "2020-S9", "2023-S16", "2025-E2"],
 "6.2-b": ["2017-S5"],
 "6.2-c": ["2008-S13", "2013-E9"],
 "6.3-a": ["2005-S7", "2011-S6"],
 "6.3-b": ["2006-X4", "2009-S17", "2020-S8"],
 "6.3-c": ["2009-S20", "2005-E1", "2007-S20"],
 "6.4-a": ["2024-E10", "2025-S23"],
 "6.4-b": ["2018-S24", "2018-S25", "2017-S25", "2008-E7", "2023-E9", "2006-S14"],
 "6.4-c": ["2007-S13", "2011-S16", "2010-S7", "2023-S21", "2019-S12", "2020-X1", "2014-S22"],
 "6.4-d": ["2022-E11", "2025-E10", "2016-X1", "2014-X6", "2015-X6", "2007-X4"],
 "6.4-g": ["2016-E10", "2018-E8", "2017-E9"],
 "6.5-a": ["2013-S4", "2021-S1", "2014-E12"],
 "6.5-b": ["2005-E7", "2013-E12", "2019-E11", "2020-E8", "2020-E11", "2023-S10", "2025-E12", "2011-X3", "2008-E5"],
 "6.5-c": ["2012-S18", "2018-X3", "2020-X4"],
 "7.1-a": ["2024-S14", "2013-S9", "2012-E7"],
 "7.1-b": ["2010-X2", "2011-E3", "2019-S24", "2023-S25", "2009-X1"],
 "7.2-a": ["2019-E13"],
 "7.2-b": ["2024-E4", "2021-S16", "2013-S25", "2005-E8", "2020-X5"],
 "7.3-a": ["2006-S16", "2009-S16", "2015-X5", "2023-X5", "2023-E4", "2017-X2", "2025-S15"],
 "7.3-b": ["2005-S20", "2018-S17", "2018-S21", "2013-S18", "2019-E6", "2011-X1", "2005-X3", "2025-X6"],
 "7.4-a": ["2025-S5", "2019-S19", "2011-E11", "2023-S12"],
 "7.4-b": ["2005-S2", "2006-X5", "2011-E7", "2010-X6", "2013-S16"],
 "7.4-c": ["2015-S23", "2014-S13", "2017-S22"],
 "7.4-d": ["2020-S15", "2011-E4", "2025-S6"],
 "7.4-e": ["2014-S20", "2016-X5", "2020-X3", "2023-X3"],
 "8.1-a": ["2012-S11", "2017-S3", "2009-S12", "2016-S13", "2016-S20"],
 "8.1-b": ["2024-S1", "2006-S5", "2007-S21", "2019-S8", "2012-E4", "2011-E2"],
 "8.1-c": ["2007-S25", "2023-S13", "2022-X5", "2017-E4"],
 "8.2-a": ["2005-X4", "2018-S13", "2018-S3", "2017-S20", "2023-S11", "2025-S1", "2018-X5"],
 "8.3-a": ["2007-S11", "2016-E11", "2005-X1", "2006-X1", "2006-S10", "2010-S5", "2019-E5"],
 "8.3-b": ["2023-S9", "2022-S4", "2006-X3", "2007-X1"],
}

# Leaves that only IMSO needs: sub-group -> [(title, sign, key, examples)]
NEW = {
"1.1": [
 ("Chia hết cho 7, 11, 13 và số có chữ số lặp", "số 333…3 chia hết cho 383; số 66…6x chia hết cho 7", "1001 = 7 × 11 × 13 nên abcabc chia hết cho 7, 11 và 13; 111111 = 3 × 7 × 11 × 13 × 37. Cắt số dài thành các khối lặp lại rồi xét số dư của từng khối.", ["2008-S14", "2013-E8", "2017-E3", "2019-X1", "2016-E5"]),
 ("Giai thừa chia cho một tổng", "1 × 2 × … × 15 chia cho 1 + 2 + … + 15; hai chữ số cuối của 1! + 2! + … + 2025!", "1 + 2 + … + n = n(n + 1)/2. Phân tích tổng ra thừa số rồi kiểm tra n! có chứa đủ các thừa số đó không. Từ 10! trở đi, giai thừa tận cùng bằng 00.", ["2014-S19", "2010-E2", "2025-S18"]),
],
"1.2": [
 ("Tổng bằng tích", "100 số nguyên dương có tổng bằng tích", "Thêm số 1 làm tổng tăng mà tích không đổi. Chọn vài số lớn hơn 1, rồi bù số lượng còn thiếu bằng các số 1.", ["2020-X6"]),
],
"1.4": [
 ("Hiệu hai bình phương và bộ ba Pythagore", "N và N + 97 đều là số chính phương; tam giác vuông có một cạnh là 12", "b² − a² = (b − a)(b + a). Với tam giác vuông có cạnh góc vuông a: (c − b)(c + b) = a², rồi liệt kê các cặp ước cùng tính chẵn lẻ.", ["2005-S11", "2017-S19", "2025-S20", "2009-Q8", "2023-E2"]),
 ("So sánh và biến đổi lũy thừa", "số nào lớn nhất trong các lũy thừa; các tờ tiền là lũy thừa của 7", "Đưa về cùng cơ số hoặc cùng số mũ: a^(mn) = (a^m)^n. Biểu diễn một số theo lũy thừa của 7 chính là viết số đó ở hệ cơ số 7.", ["2008-E1", "2025-E13", "2014-X2"]),
],
"2.1": [
 ("Tuổi bằng tổng chữ số của năm sinh", "tuổi năm 2023 bằng tổng các chữ số của năm sinh", "Viết năm sinh dạng 19ab hoặc 20ab. Tuổi = năm hiện tại − năm sinh = tổng chữ số. Lập phương trình theo a, b rồi thử các chữ số.", ["2017-E2", "2019-E2", "2020-S1", "2023-S24"]),
 ("Số tạo bằng cách chuyển chữ số", "bỏ chữ số đầu thì số mới bằng 1/26 số cũ; abcdef × 6 = defabc", "Đặt phần còn lại là x: 5·10⁵ + x = 26x. Với abcdef × 6 = defabc, đặt abc = x, def = y rồi lập phương trình (1000x + y) × 6 = 1000y + x.", ["2005-S8", "2023-S4", "2023-E6", "2014-E10"]),
],
"2.2": [
 ("Chèn số hoặc dấu để được kết quả cho trước", "chèn dấu + và − vào 123456789 để được 100; sáu số có chữ số 6 có tổng 100", "Bắt đầu từ phần đóng góp lớn nhất (số nhiều chữ số), rồi điều chỉnh bằng các số nhỏ. Dùng tính chẵn lẻ và số dư khi chia 9 để loại bớt.", ["2013-X4", "2019-S10", "2014-S11", "2019-S9"]),
],
"2.3": [
 ("Đồng hồ số", "bao nhiêu phút đồng hồ hiện chữ số 3; tổng chữ số của giờ bằng tổng chữ số của phút", "Đếm riêng phần giờ và phần phút rồi kết hợp. Tách các khoảng giờ có cùng tính chất để không đếm trùng.", ["2020-S17", "2022-E2"]),
],
"3.1": [
 ("Đặt phép toán để được giá trị lớn nhất", "đặt +, −, × vào các ô trống", "Liệt kê có hệ thống mọi cách đặt. Nhớ phép nhân, chia được thực hiện trước phép cộng, trừ.", ["2015-S3", "2020-S6"]),
 ("Tính tổng bằng ghép cặp và công thức", "hiệu giữa tổng các số chẵn và tổng các số lẻ; tổng các lập phương", "Ghép số đầu với số cuối. 1³ + 2³ + … + n³ = (n(n + 1)/2)². Một tổng gồm nhiều tích có thể viết lại thành tích của các tổng.", ["2023-E1", "2021-E11", "2012-S17"]),
],
"3.2": [
 ("Cho đi từng phần: tính ngược từ cuối", "cho đi một nửa và thêm 13; giữ một nửa, chia nửa còn lại", "Đi ngược từ kết quả cuối cùng. Nếu cho đi 1/2 rồi thêm 13 mà còn lại R thì trước đó có 2 × (R + 13).", ["2007-E4", "2013-S17", "2014-S14", "2016-S6", "2021-S17"]),
 ("Pha trộn và tỉ lệ thay đổi", "nước cam nguyên chất trong bình; rót trà qua lại giữa hai cốc", "Theo dõi riêng lượng của từng thành phần. Thành phần không đổi giúp tìm tổng mới.", ["2011-S13", "2011-S25", "2015-S5", "2008-S6"]),
],
"3.3": [
 ("Lãi và lỗ", "một chiếc lãi 30%, một chiếc lỗ 30%; bán 80% với lãi 30%", "Lãi 30% nghĩa là giá bán = 1,3 × giá vốn; lỗ 30% nghĩa là giá bán = 0,7 × giá vốn. Tính tổng vốn và tổng tiền bán rồi so sánh.", ["2016-S8", "2019-S2", "2022-E1"]),
 ("Thành phần không đổi (bài dưa hấu)", "97% là nước, sau khi phơi chỉ còn 90%", "Phần không thay đổi (chất khô) giữ nguyên khối lượng. Dùng phần đó để tính tổng khối lượng mới.", ["2005-S14", "2006-E7", "2017-E6"]),
],
"3.4": [
 ("Trung vị, mốt và trung bình", "trung bình 88, trung vị 89, mốt 93", "Sắp xếp các số theo thứ tự. Trung vị là số ở giữa, mốt là số xuất hiện nhiều nhất, tổng = trung bình × số lượng.", ["2011-S14", "2015-S22", "2013-S3"]),
],
"3.5": [
 ("Trao đổi giữa các bạn", "nếu A cho B 30 đô thì B có gấp đôi A", "Mỗi câu “nếu A cho B …” cho một phương trình. Khi trao đổi trong nhóm, tổng của cả nhóm không đổi.", ["2009-S10", "2009-Q4", "2016-S14", "2017-S6", "2008-Q1"]),
 ("Bất đẳng thức và nghiệm nguyên", "cân nặng là số nguyên, thêm 6 kg thì dưới 36 kg", "Viết các điều kiện “ít hơn, nhiều hơn” thành bất đẳng thức rồi chọn nghiệm nguyên phù hợp.", ["2007-S2", "2008-S10", "2022-S2"]),
],
"4.1": [
 ("Đến sớm, đến muộn", "đi 50 km/h thì muộn 2 phút, đi 60 km/h thì sớm 1 phút", "Chênh lệch thời gian = d/v₁ − d/v₂. Lập phương trình theo quãng đường d.", ["2006-E6", "2010-E7", "2012-E6"]),
],
"4.2": [
 ("Lịch và ngày trong tuần", "53 ngày thứ Ba trong một năm; ngày 28 là thứ mấy", "Các thứ lặp lại sau mỗi 7 ngày. Sang năm mới, thứ của cùng một ngày dịch 1 (năm thường) hoặc 2 (năm nhuận).", ["2009-S5", "2010-S9", "2011-E1", "2013-S13", "2016-S9", "2021-E8"]),
],
"4.3": [
 ("Làm chung một công việc", "A làm một mình hết 6 giờ, B hết 10 giờ", "Năng suất = 1 / thời gian. Làm chung thì cộng năng suất. Hai người cùng làm trong t giờ: t × (tổng năng suất) = 1.", ["2011-S10", "2016-S1", "2016-S21", "2018-S1", "2023-S22", "2009-Q7", "2009-S6"]),
 ("Chia đều quãng đường hoặc phương tiện", "6 lốp xe chạy đều cho 24.000 km; ba bạn dùng chung hai xe đạp", "Tính tổng “công” cần làm (quãng đường × số bánh đang lăn, …) rồi chia đều. Với xe dùng chung, vẽ sơ đồ thời gian cho từng người.", ["2009-S18", "2014-S21", "2013-S24"]),
],
"5.1": [
 ("Diện tích trên lưới điểm", "đa giác vẽ trên lưới ô vuông 1 cm", "Bao hình bằng một hình chữ nhật rồi trừ các tam giác vuông ở góc. Hoặc dùng công thức Pick: S = I + B/2 − 1 (I điểm bên trong, B điểm trên cạnh).", ["2012-S15", "2018-S4"]),
],
"5.2": [
 ("Gấp giấy và góc", "gấp tờ giấy ba lần; gấp hình vuông theo DP", "Phần bị gấp đối xứng qua nếp gấp nên các góc tương ứng bằng nhau. Các góc tại một điểm trên đường thẳng có tổng 180°.", ["2014-S12", "2025-S7"]),
 ("Tam giác đồng dạng và bóng nắng", "bóng của tòa nhà và cột; ba đoạn thẳng song song", "Tia nắng song song tạo ra các tam giác đồng dạng. Tỉ số chiều cao bằng tỉ số độ dài bóng.", ["2006-E8", "2010-E5", "2012-E10"]),
],
"5.3": [
 ("Hình vuông và hình tròn lồng nhau", "hình tròn nội tiếp hình vuông lớn, hình vuông nhỏ nội tiếp hình tròn", "Hình vuông nội tiếp đường tròn có đường chéo bằng đường kính, nên diện tích bằng 2r². Hình tròn nội tiếp hình vuông có đường kính bằng cạnh.", ["2007-S3", "2010-S6", "2008-S15", "2007-S10"]),
 ("Lăn quanh một hình", "tam giác đều lăn quanh ngũ giác đều; đĩa lăn quanh mặt đồng hồ", "Vết của một điểm gồm các cung tròn; cộng các góc quay ở mỗi đỉnh. Đĩa bán kính r lăn quanh đĩa bán kính R thì tự quay (R + r)/r vòng.", ["2020-S25", "2021-S24", "2017-S2"]),
 ("Góc nội tiếp và dây cung", "AB là đường kính, tìm góc ACD", "Góc nội tiếp bằng nửa số đo cung bị chắn. Góc nội tiếp chắn nửa đường tròn là góc vuông.", ["2007-E12", "2008-Q12", "2017-S13", "2005-E9"]),
],
"5.4": [
 ("Hình chữ nhật ghép từ các hình vuông", "hình chữ nhật chia thành các hình vuông khác nhau", "Đặt cạnh hình vuông nhỏ nhất là x, biểu diễn cạnh các hình vuông khác theo x, rồi dùng điều kiện hai cạnh đối của hình chữ nhật bằng nhau.", ["2019-S6", "2022-S12", "2014-E13", "2025-E3", "2025-S3", "2013-S22"]),
 ("Gấp giấy và độ dài", "gấp tờ giấy vuông theo MN; gấp phong bì", "Phần gấp chồng khít lên phần đối xứng của nó. Lập phương trình diện tích phần nhìn thấy hoặc dùng Pythagore.", ["2011-S19", "2019-E9"]),
 ("Đối xứng và hình phản chiếu", "chữ viết trên cửa kính nhìn từ phía bên kia; lá bài bị xoay 180°", "Ảnh qua gương đảo trái và phải. Xoay 180° thì hình đảo cả trên dưới lẫn trái phải.", ["2008-S1", "2012-S24"]),
],
"5.5": [
 ("Xúc xắc và các mặt đối diện", "hai mặt đối diện có tổng 7; lăn xúc xắc theo đường đi", "Hai mặt đối diện có tổng 7. Khi lăn, theo dõi mặt trên, mặt trước và mặt phải sau mỗi bước.", ["2006-S17", "2010-S23", "2010-X1", "2020-S13"]),
 ("Hình chiếu và hình nhìn từ các phía", "nhìn từ trước, từ cạnh, từ trên", "Số khối lớn nhất: mỗi cột cao bằng giá trị nhỏ hơn trong hai hình chiếu. Số khối nhỏ nhất: chỉ cần đủ để mỗi hình chiếu đạt được chiều cao của nó.", ["2010-X3", "2019-X6"]),
 ("Hình hộp biết diện tích các mặt", "ba mặt có diện tích 35, 55 và 77", "Nếu ba mặt có diện tích ab, bc, ca thì (abc)² = ab · bc · ca, nên thể tích bằng căn bậc hai của tích ba diện tích.", ["2010-S8", "2009-S15"]),
],
"6.1": [
 ("Bao hàm – loại trừ với hai tập (sơ đồ Venn)", "thích toán, thích MTV, không thích cả hai", "|A ∪ B| = |A| + |B| − |A ∩ B|. Số người không thuộc tập nào = tổng số − |A ∪ B|.", ["2011-S23", "2012-S9", "2015-S9"]),
 ("Xác suất", "xác suất bỏ lỡ cuộc gọi; tung hai xúc xắc", "Xác suất = số kết quả thuận lợi / tổng số kết quả đồng khả năng. Với thời gian liên tục, dùng tỉ số độ dài các khoảng.", ["2011-S24", "2021-S25", "2022-S21"]),
 ("Đếm tam giác tạo từ các điểm", "có bao nhiêu tam giác từ 6 điểm; tam giác tù từ 7 điểm trên đường tròn", "Chọn 3 điểm: C(n, 3) cách, rồi trừ các bộ ba điểm thẳng hàng. Với điểm trên đường tròn, phân loại theo cung lớn nhất.", ["2005-E4", "2011-S18", "2020-S14", "2021-S20"]),
 ("Chèn dấu giữa các chữ số", "chèn dấu + vào 777…7 để được bội của 30", "Mỗi khe giữa hai chữ số có dấu hoặc không: 2^(số khe) cách. Lọc theo điều kiện chia hết của kết quả.", ["2020-E1", "2021-X2", "2022-E4"]),
],
"6.2": [
 ("Tích hoặc tổng chữ số cho trước", "tích các chữ số bằng 360; tổng chữ số bằng 9", "Phân tích tích thành các thừa số nhỏ hơn 10 (360 = 5 × 8 × 9 = …), liệt kê các bộ chữ số có thể, rồi đếm số hoán vị của từng bộ.", ["2005-E3", "2018-S10", "2025-S25", "2016-E9", "2014-S8", "2018-E12"]),
],
"6.3": [
 ("Đếm tam giác và các hình trong hình vẽ", "có bao nhiêu tam giác đều trong hình", "Đếm theo kích thước và theo hướng (đỉnh lên, đỉnh xuống). Chia thành các lớp để không đếm trùng.", ["2016-S22", "2017-S8", "2009-Q9", "2017-E12", "2018-E2"]),
 ("Đường thẳng chia mặt phẳng", "n đường thẳng chia mặt phẳng; chia hình vuông thành tam giác với các điểm bên trong", "Đường thẳng mới cắt k đường cũ thì tạo thêm k + 1 miền. Chia hình vuông có n điểm bên trong thành tam giác thì được 2n + 2 tam giác.", ["2006-S11", "2012-X3", "2021-S7", "2018-S18"]),
],
"6.4": [
 ("Chọn các ô không kề nhau", "đánh dấu 5 ô không kề nhau trên bảng 2 × 7", "Lập truy hồi theo từng cột: trạng thái của cột trước quyết định các lựa chọn của cột sau.", ["2023-E13", "2018-E13", "2024-X5"]),
],
"7.1": [
 ("Suy luận từ các dự đoán", "mỗi khán giả đoán thứ hạng của hai người", "Lập bảng các dự đoán, thử từng giả thiết rồi loại các trường hợp mâu thuẫn.", ["2019-S3", "2020-E3", "2020-S21"]),
 ("Đoán mã từ các gợi ý", "mã thẻ ATM; khóa số 6 chữ cái; túi bi đỏ", "Dùng từng gợi ý để loại trừ. Bắt đầu từ gợi ý mạnh nhất (vị trí cố định, chẵn lẻ, tổng).", ["2008-Q9", "2009-Q11", "2010-E4", "2015-S20"]),
],
"7.3": [
 ("Vòng số có tổng là số nguyên tố hoặc chính phương", "hai số kề nhau có tổng là số nguyên tố", "Xét chẵn lẻ: tổng lẻ thì hai số kề nhau phải khác tính chẵn lẻ. Bắt đầu từ số có ít số ghép được nhất.", ["2010-S17", "2012-E13", "2016-E1", "2020-E2"]),
 ("Tam giác hiệu số", "mỗi số là hiệu của hai số phía trên", "Số lớn nhất phải nằm ở hàng trên cùng. Thử đặt số lớn nhất trước, rồi điền dần các hàng dưới.", ["2013-X6", "2015-S7", "2014-X5"]),
],
"7.4": [
 ("Cân để tìm đồng xu giả", "tìm đồng xu nặng hơn hoặc nhẹ hơn với ít lần cân nhất", "Mỗi lần cân có 3 kết quả, nên k lần cân phân biệt được tối đa 3^k trường hợp. Chia các đồng xu thành 3 nhóm.", ["2013-E11", "2016-X3", "2020-S18", "2021-S10"]),
 ("Bất biến và chẵn lẻ trong quá trình", "thay hai số bằng hiệu của chúng; lật đồng xu theo hàng", "Tìm đại lượng không đổi sau mỗi bước (tính chẵn lẻ của tổng, số lượng theo màu) để loại trừ những kết quả không thể đạt.", ["2020-S7", "2013-S15", "2018-X4", "2021-E1"]),
],
"8.2": [
 ("Loại người theo vòng (Josephus)", "viết 1 đến 6 quanh vòng tròn, bỏ cách một số", "Mô phỏng với n nhỏ để tìm quy luật, sau đó tổng quát hóa.", ["2022-E7"]),
],
}

L = merge_leaves(KS2_L, EXAMPLES, NEW)

# All KS2 leaves followed by the IMSO-only ones: the base of the IMAS primary mind maps.
KS2_WITH_IMSO = {sub: list(KS2_L.get(sub, [])) + list(NEW.get(sub, [])) for sub in SUB_VN}
