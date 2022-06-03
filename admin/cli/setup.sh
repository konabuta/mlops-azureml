az extension add -n ml -y

GROUP=$1
WORKSPACE=$2
LOCATION=$3

az configure --defaults group=$GROUP workspace=$WORKSPACE location=$LOCATION
