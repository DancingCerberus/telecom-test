### Section 1

`python3 section_1/main.py`

### Section 2

`docker build -t httpstatus ./section_2`

`docker run --name myhttp httpstatus`

`docker logs myhttp`

### Section 3

`ansible-playbook -i inventory.ini playbook.yml -K`