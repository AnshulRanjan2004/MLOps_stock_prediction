GROUP="stock_prediction"
LOCATION="eastus"
WORKSPACE="stock_prediction"

az configure --defaults group=$GROUP workspace=$WORKSPACE location=$LOCATION

az extension remove -n ml
az extension add -n ml
