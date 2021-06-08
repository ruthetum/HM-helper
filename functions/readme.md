## 개요
- 실험은 8K 영상 3개를 2x4, 3x6, 6x12 타일링을 적용한 것과 ECP를 적용한 영상을 원본 영상의 PSNR과 Bitrate를 대조하였습니다.
- 300프레임의 8K 영상을 한 번에 인코딩하는 것은 시간이 매우 소모되기 때문에 32프레임을 기준으로 분할하여 인코딩 및 디코딩을 진행하였고, 이후 Viewport를 생성하여 PSNR을 측정할 때는 영상을 다시 병합하여 PSNR을 측정하였습니다.
- 타일링 설정을 한 경우 Bitrate 측정 시 extract 과정이 필요하기 때문에 anchor와 ECP를 제외한 타일링 실험 과정에는 extract 과정이 필요합니다.

| |Encoding|Decoding|Concat|Viewport|PSNR|Extract|Bitrate|
|------|------|-----|------|-----|------|-----|------|
|<center>anchor</center>|<center>O</center>|<center>O</center>|<center>O</center>|<center>O</center>|<center>O</center>|<center>X</center>|<center>O</center>|
|<center>2x4</center>|<center>O</center>|<center>O</center>|<center>O</center>|<center>O</center>|<center>O</center>|<center>O</center>|<center>O</center>|
|<center>3x6</center>|<center>O</center>|<center>O</center>|<center>O</center>|<center>O</center>|<center>O</center>|<center>O</center>|<center>O</center>|
|<center>6x12</center>|<center>O</center>|<center>O</center>|<center>O</center>|<center>O</center>|<center>O</center>|<center>O</center>|<center>O</center>|
|<center>ECP</center>|<center>O</center>|<center>O</center>|<center>O</center>|<center>O</center>|<center>O</center>|<center>X</center>|<center>O</center>|

## Encoding
#### generate_8K_encoding_chunk_cmdline.py
- 인코딩 쉘 스크립트 작성
```
python3 generate_8K_encoding_chunk_cmdline.py encoding_8k.sh
```
- argv[1] : 작성할 쉘 스크립트의 이름

## Decoding
#### generate_8K_decoding_chunk_cmdline.py
- 디코딩 쉘 스크립트 작성
```
python3 generate_8K_decoding_chunk_cmdline.py decoding_8k.sh
```
- argv[1] : 작성할 쉘 스크립트의 이름

## Concat
#### concat_0-299.py
- 분할된 영상 합칠 쉘 스크립트 작성 (300프레임)
```
python3 concat_0-299.py concat_8k.sh
```
- argv[1] : 작성할 쉘 스크립트의 이름

## Viewport
#### generate_8K_viewport.py
- 뷰포트 생성 쉘 스크립트 작성
```
python3 generate_8k_viewport.py viewport_8k.sh
```
- argv[1] : 작성할 쉘 스크립트의 이름

### PSNR
#### wspsnr_posetrace.py
- PSNR 측정 쉘 스크립트 작성
```
python3 wspsnr_posetrace.py psnr_8k.sh
```
- argv[1] : 작성할 쉘 스크립트의 이름



- <code>get_WSPSNR_log_write_wspsnr.py</code> :

### Extract
- <code>generate_8K_extractor_cmdline_option1.py</code> : 


- <code>generate_8K_extractor_cmdline_option2.py</code> :

### Bitrate
- <code>get_chunklist_write_bitrate_anchor.py</code> : 


- <code>get_chunklist_write_bitrate_tile.py</code> : 


- <code>get_tilelist_write_bitrate_AerialCity.py</code> : 

### Etc.

- <code>split_cmdline.py</code>
    - 쉘 스크립트 분할 
  
15 : number to split
  
  Ex)
  All length : 150
  Number of split : 15
  Splited shell script file : 10

---  
### Tip
#### 인코딩 과정
  ```
  # Make encoding shell script
  python3 generate_8K_encoding_chunk_cmdline.py encoding_8k.sh
  
  # Split encoding shell script
  python3 /data/vs/split_cmdline.py encoding_8k.sh 15 run_encoding_8k.sh
  
  # [Option] Change mode to execute shell script
  chmod +x *.sh
  
  # Execute shell script
  ./run_encoding_8k.sh
  ```
