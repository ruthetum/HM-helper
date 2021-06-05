# Sample Architecture

```bash
sample-architecture
    ├── 2x4
    ├── 3x6
    ├── 6x12
    ├── anchor
    │   ├── config_files
    │   ├── enc_chunk
    │   ├── concat_0-299.py
    │   ├── generate_8K_decoding_chunk_cmdline.py
    │   ├── ...    
    │   └── get_chunklist_write_bitrate_anchor.py.py
    └── ecp
```

- 2x4, 3x6, 6x12 타일링 설정에 따라 분류
- anchor : 타일링 설정 또는 ECP 적용한 값과 대조를 위한 기본 영상을 인코딩, 디코딩
- ecp : ECP 적용

