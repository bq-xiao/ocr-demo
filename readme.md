## OCR Demo

Python版本：Python 3.8.6

### 依赖Python库
```shell script
pip install easyocr
pip install twisted
pip install logging
```

### How to start OCR server
```shell script
# python.exe ocr_server.py
# usage: ocr_server.py -p <port>

# python.exe ocr_server.py -p 8001
2020-11-04 18:08:23,224 - easyocr.easyocr - WARNING - CUDA not available - defaulting to CPU. Note: This module is much faster with a GPU.
2020-11-04 18:08:26,092 - __main__ - INFO - TCP server started on port(s): 8001 ...

```

### How to start client
```shell script
# python.exe ocr_client.py
# usage: ocr_client.py -h <host> -p <port> -i <image>
# python.exe ocr_client.py -h localhost -p 8001 -i chinese.jpg
2020-11-04 18:08:30,410 - __main__ - INFO - Start time: 2020-11-04 18:08:30
2020-11-04 18:08:34,069 - __main__ - INFO - Got response: 愚园路西东315309Yuyuan Rd.WE

2020-11-04 18:08:34,069 - __main__ - INFO - End time: 2020-11-04 18:08:34

```
