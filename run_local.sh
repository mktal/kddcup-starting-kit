# @Author: Xiaocheng Tang
# @Date:   2020-03-24 23:46:19
# @Last Modified by:   Xiaocheng Tang
# @Last Modified time: 2020-03-24 23:49:00


set -e
DIR="$( cd "$( dirname "${BASH_SOURCE[0]}" )" >/dev/null 2>&1 && pwd )"
cd "$DIR"

docker build -t kddcup -f Dockerfile .
docker run -it kddcup --rm
