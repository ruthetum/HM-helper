# 3x6 tiling

- anchor 디렉토리 구조와 거의 동일
- 다만 타일링의 경우 bitrate를 측정하기 위해서는 extract 과정이 필요함
- enc_chunk 내의 분할된 프레임 내부에 extractor 디렉토리가 존재함
```bash
   3x6
    ├── config_files
    │   ├── 360test_DynamicViewports.cfg
    │   ├── 8192x4096_32frames_cfg.cfg
    │   ├── ...
    │   └── viewport_option2.txt
    │
    ├── enc_chunk
    │   ├── 0-31
    │   │   ├── dec_log
    │   │   ├── enc_log
    │   │   ├── "extractor"
    │   │   ├── files_decoded
    │   │   ├── files_encoded
    │   ├── 32-63
    │   ├── 64-95
    │   ├── 96-127
    │   ├── ...
    │   ├── 288-299
    │   ├── concat
    │   └── viewport
    │
    ├── concat_0-299.py
    ├── generate_8K_decoding_chunk_cmdline.py
    ├── ...    
    └── get_chunklist_write_bitrate_anchor.py.py
```
- 실행 파일 및 설정 파일의 내용에 약간의 차이가 존재하기 때문에 실행 파일 및 설정 파일의 usage를 참고