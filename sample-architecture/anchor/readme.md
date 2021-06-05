# anchor

```bash
 anchor
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
    │   │   ├── extractor
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