# Secondary software for HEVC(HM)
- 본 저장소는 [2021년 1학기 연구학점제 실험](./experiment/readme.md)을 바탕으로 작성되었습니다.
- 또한 실험 내용 기록 및 이후 진행될 수 있는 유사 실험에 도움을 주기 위한 목적으로 작성되었습니다.
- 본 저장소는 실험을 돕기 위한 보조 프로그램으로 작성되었기 때문에 [HEVC reference model (HM)](https://vcgit.hhi.fraunhofer.de/jvet/HM) 과 [360Lib](https://jvet.hhi.fraunhofer.de/svn/svn_360Lib/branches/) 의 설치 및 빌드를 전제로 합니다.
- 저장소에 존재하는 소스 코드의 출처와 권리는 [Multimedia Computing Systems Lab (MCSL)](http://mcsl.skku.edu/) 에 있음을 알립니다.

## 저장소 구조
- 본 저장소는 다음과 같은 구조로 구성되어 있습니다.
    ```bash
    ├── configurations
    ├── experiment
    ├── functions 
    ├── reference
    └── sample-architecture
    ```
    |Directory|Content|
    |------|-----|
    |configurations|실험에서 사용된 설정 파일|
    |experiment|실험 관련 내용 및 설명|
    |functions|실험에서 사용된 실행 파일|
    |reference|선행 개념 및 관련 개념에 관한 설명|
    |sample-architecture|실제 실험의 디렉토리 구조|
  
- 실험의 내용 및 결과에 대해 확인할 경우 <code>experiment</code>디렉토리를 참고하면 됩니다.
- 선행 이론 및 개념에 관해 확인할 경우 <code>reference</code>디렉토리를 참고하면 됩니다.
- 유사한 실험을 진행할 때 참고용으로 본 저장소를 확인하는 경우 <code>sample-architecture</code> 디렉토리를 확인한 이후 <code>functions</code>와 <code>configurations</code> 디렉토리에서 필요한 실행 파일 및 설정 파일을 <b>경로에 맞게 실행</b> 또는 <b>복사</b>해서 사용하면 됩니다.