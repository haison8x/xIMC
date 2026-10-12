# xIMC

Tài liệu ôn luyện IMC và IMSO: đề gốc, đề trích xuất dạng văn bản, phân loại theo dạng bài và mindmap ôn tập.
Website: https://haison8x.github.io/xIMC/

## Cấu trúc thư mục

```
├── index.html, ximc.html, imso.html   Trang web (GitHub Pages phục vụ từ thư mục gốc)
├── mindmaps/                          Mindmap ôn tập (sinh bởi build_mindmaps.py)
├── data/                              Đề trích xuất và bảng phân loại dạng .txt (sinh bởi script)
├── papers/                            Đề gốc PDF
│   ├── imc/keystage2/, imc/keystage3/   {năm}.pdf, {năm}_team.pdf, {năm}_answer.pdf
│   ├── imso/                            ShortAnswer/, Essay/, Exploration/, Answers/
│   └── imas/                            middle_primary/, upper_primary/, junior/, answers/ → {năm học}_round{1,2}.pdf
└── scripts/                           Script Python
    ├── crawl_imc.py                     Tải đề IMC về papers/imc/
    ├── crawl_imas.py                    Tải đề IMAS về papers/imas/
    ├── extract_imc.py, extract_imso.py  Trích đề từ PDF ra data/*_problems.txt
    ├── categorize.py, categorize_imso.py  Bảng phân loại thủ công → data/*_categories.txt
    ├── leaves_*.py                      Các kỹ thuật (lá) của mindmap
    ├── build_mindmaps.py, mindmap_template.html  Sinh mindmaps/*.html
    └── paths.py                         Đường dẫn dùng chung
```

## Chạy lại pipeline

```
pip install pymupdf
python scripts/crawl_imc.py        # chỉ tải đề còn thiếu
python scripts/crawl_imas.py       # chỉ tải đề còn thiếu
python scripts/extract_imc.py
python scripts/extract_imso.py
python scripts/build_mindmaps.py   # ghi lại data/*_categories.txt và mindmaps/*.html
```
