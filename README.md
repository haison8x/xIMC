# xIMC

Tài liệu ôn luyện IMC, IMSO, IMAS và IGO: đề gốc, đề trích xuất dạng văn bản, phân loại theo dạng bài và mindmap ôn tập.
Website: https://haison8x.github.io/xIMC/

## Cấu trúc thư mục

```
├── index.html, ximc.html, imso.html, imas.html, igo.html   Trang web (GitHub Pages phục vụ từ thư mục gốc)
├── mindmaps/                          Mindmap ôn tập (sinh bởi build_mindmaps.py)
├── data/                              Đề trích xuất và bảng phân loại dạng .txt (sinh bởi script)
├── papers/                            Đề gốc PDF
│   ├── imc/keystage2/, imc/keystage3/   {năm}.pdf, {năm}_team.pdf, {năm}_answer.pdf
│   ├── imso/                            ShortAnswer/, Essay/, Exploration/, Answers/
│   ├── imas/                            middle_primary/, upper_primary/, junior/, answers/ → {năm học}_round{1,2}.pdf
│   └── igo/                             IGO{năm}.pdf (sách đề + lời giải)
└── scripts/                           Script Python
    ├── crawl_imc.py                     Tải đề IMC về papers/imc/
    ├── crawl_imas.py                    Tải đề IMAS về papers/imas/
    ├── extract_imc.py, extract_imso.py, extract_imas.py, extract_igo.py  Trích đề từ PDF ra data/*_problems.txt
    ├── categorize.py, categorize_imso.py, categorize_imas.py, categorize_igo.py  Bảng phân loại thủ công → data/*_categories.txt
    ├── leaves_*.py, leaves_util.py      Các kỹ thuật (lá) của mindmap
    ├── build_mindmaps.py, mindmap_template.html  Sinh mindmaps/*.html
    └── paths.py                         Đường dẫn dùng chung
```

## Nguồn đề

| Kỳ thi | Cách lấy đề |
|---|---|
| IMC | `scripts/crawl_imc.py` tải từ chiuchang.org |
| IMAS | `scripts/crawl_imas.py` tải từ chiuchang.org |
| IMSO | Tải tay, đặt vào `papers/imso/{ShortAnswer,Essay,Exploration,Answers}/` |
| IGO | Tải tay sách "Problems and Solutions" bản có chữ (không dùng bản scan), đặt thành `papers/igo/IGO{năm}.pdf` |

## Chạy lại pipeline

```
pip install pymupdf
python scripts/crawl_imc.py        # chỉ tải đề còn thiếu
python scripts/crawl_imas.py       # chỉ tải đề còn thiếu
python scripts/extract_imc.py
python scripts/extract_imso.py
python scripts/extract_imas.py
python scripts/extract_igo.py
python scripts/build_mindmaps.py   # ghi lại data/*_categories.txt và mindmaps/*.html
```

## Cách phân loại hoạt động

Phân loại là **dữ liệu gõ tay**, không có thuật toán tự động. Mỗi kỳ thi có hai phần:

- **Nhánh con của từng bài**: bảng mã trong `scripts/categorize*.py`, mỗi đề một chuỗi mã theo đúng thứ tự bài trong `data/*_problems.txt`.
  - IMC: `individual` / `team` trong `categorize.py`, ví dụ `2024: "3.3 2.3 4.2 …"`.
  - IMSO, IMAS, IGO: `CODES`, ví dụ `2024: dict(E="1.1 2.2 3.1 5.1 6.1", I="…", A="…")` cho IGO.
- **Dạng bài (lá)**: `scripts/leaves_*.py`, mỗi nhánh con có danh sách `(tên dạng, dấu hiệu nhận biết, chìa khóa, [bài ví dụ])`.
  - IMSO và IMAS dùng lại lá của IMC (qua `leaves_util.merge_leaves`), rồi thêm lá riêng.
  - IGO có hệ nhánh hình học riêng (7 nhánh, 21 nhánh con) và toàn bộ lá riêng.

`build_mindmaps.py` dừng với thông báo lỗi nếu số mã không khớp số bài, có mã không tồn tại, có bài chưa được phân loại, hoặc bài ví dụ của một lá không thuộc đúng nhánh con của lá đó.

## Thêm đề năm mới

1. Đặt PDF vào `papers/…` (chạy crawl hoặc tải tay).
2. Chạy script `extract_*.py` của kỳ thi đó, rồi kiểm tra file `data/*_problems.txt`: đủ số bài và văn bản sạch.
3. Thêm dòng mã cho năm mới vào bảng phân loại. Nếu muốn, thêm các bài mới làm ví dụ cho lá trong `leaves_*.py`.
4. Chạy `build_mindmaps.py`.
5. Sửa tay các con số và danh sách năm đang ghi cố định trên trang web:
   - số bài và số dạng bài trong `index.html`, `ximc.html`, `imso.html`, `imas.html`, `igo.html`;
   - danh sách năm: `YEARS` trong `ximc.html`, `ROWS` trong `imso.html`, `from`/`to` trong `imas.html`, vòng lặp năm trong `igo.html`.

## Thêm một kỳ thi mới

Làm theo mẫu IGO (một mindmap) hoặc IMAS (nhiều mindmap, mỗi cấp một file):

1. `scripts/extract_<kỳ thi>.py`: trích đề ra `data/<kỳ thi>_problems.txt`. Dùng lại `extract_imc.page_lines` và `extract_imso.split_sequences`.
2. `scripts/categorize_<kỳ thi>.py`: có `KINDS` (các loại đề, hiện thành chip lọc), `load()` trả về `(bài, {mã bài: nhánh con}, hệ nhánh)` cùng dạng với `categorize_imso.load`, và `write_categories()`.
3. `scripts/leaves_<kỳ thi>.py`: có `GROUP_VN`, `SUB_VN` và `L`.
4. Thêm một mục vào `PAGES` trong `build_mindmaps.py`. Template dùng chung `mindmap_template.html` không cần sửa.
5. Viết trang giới thiệu `<kỳ thi>.html` theo mẫu `igo.html`, thêm một thẻ vào `index.html`, và cập nhật README.

**Lưu ý:** không đổi `ls_key` của một trang đã đưa lên web. Tiến độ ôn (màu thành thạo, ghi chú bẫy) được lưu trên trình duyệt theo khóa này; đổi khóa thì người học mất tiến độ.
