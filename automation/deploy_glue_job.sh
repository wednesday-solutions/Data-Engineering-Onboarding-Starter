#! /bin/bash

# Loop over all files in src/scripts/
for file in src/scripts/*.py
do
    # Get the filename without the extension
    filename=$(basename -- "$file")
    filename="${filename%.*}"

    s3_path="s3://sample-glue-wednesday/scripts"

    # Set the script name in the glue_job.json file using jq
    json_data=$(jq --arg SCRIPT_NAME "$filename" '.JobName=$SCRIPT_NAME' automation/update_glue_job.json)
    json_data=$(jq --arg LOCATION "$s3_path/$filename.py" '.JobUpdate.Command.ScriptLocation=$LOCATION' <<< $json_data)

    # Update the glue job
    aws glue update-job --cli-input-json "$json_data" --profile default
done
