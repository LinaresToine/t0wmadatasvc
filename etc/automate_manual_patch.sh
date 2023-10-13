#!/bin/bash

cd /data/srv/current/sw/slc7_amd64_gcc630/cms/t0wmadatasvc/2.0.7/lib/python3.8/site-packages/
wget https://raw.githubusercontent.com/dmwm/t0wmadatasvc/7ba07874108cda64830df8adef1c8b137ff81a60/src/python/DataExpressConfig.py
wget https://raw.githubusercontent.com/dmwm/t0wmadatasvc/d18437971a43d6d55eb32fe77168c68a5a833bb7/src/python/DataExpressConfigHistory.py
wget https://raw.githubusercontent.com/dmwm/t0wmadatasvc/7ba07874108cda64830df8adef1c8b137ff81a60/src/python/DataRecoConfig.py
wget https://raw.githubusercontent.com/dmwm/t0wmadatasvc/7ba07874108cda64830df8adef1c8b137ff81a60/src/python/DataRecoConfigHistory.py
wget https://raw.githubusercontent.com/dmwm/t0wmadatasvc/7ba07874108cda64830df8adef1c8b137ff81a60/src/python/Regexps.py

mv *.py /data/srv/current/sw/slc7_amd64_gcc630/cms/t0wmadatasvc/2.0.7/lib/python3.8/site-packages/T0WmaDataSvc

/data/srv/current/config/t0wmadatasvc/manage start 'I did read documentation'
