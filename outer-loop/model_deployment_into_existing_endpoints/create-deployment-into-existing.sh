job_flag=$(az ml online-endpoint list --query "[].name | contains(@,'lgb-endpoint-stage')")
if [ $job_flag == "true" ]; then
    az ml online-endpoint delete --name lgb-endpoint-stage --yes
else
    echo "Endpoint lgb-endpoint-stage doesn't exist."
fi
az ml online-endpoint create --name lgb-endpoint-stage


job_flag=$(az ml online-endpoint list --query "[].name | contains(@,'lgb-endpoint-prod')")
if [ $job_flag == "true" ]; then
    az ml online-endpoint delete --name lgb-endpoint-prod --yes
else
    echo "Endpoint lgb-endpoint-prod doesn't exist."
fi
az ml online-endpoint create --name lgb-endpoint-prod