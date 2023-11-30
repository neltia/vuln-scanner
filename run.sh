docker run -d --name trivy-api \
--mount type=bind,source=/etc/docker/upload-images,target=/usr/share/docker/upload-images,readonly \
-p 7000:7000 \
-v /var/run/docker.sock:/var/run/docker.sock \
trivy-api sleep infinity
