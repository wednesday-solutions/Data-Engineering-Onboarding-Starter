#! /bin/bash

# First argument is the S3 path to the scripts
s3_path="$1"

# Loop over all files in src/scripts/
for directory in src/scripts/*;
do
    # Extract the filename from the directory path
    dir_path="${directory%/}"
    file_name="${dir_path##*/}"

    if [ -e "$dir_path/main.py" ]; then
      # Check if the job exists, if not create it, else update it
      job_exists=$(aws glue get-job --job-name $file_name | jq -r .Job.Name)

      if [ "$job_exists" != "$file_name" ]; then
        # Set the script name in the glue_job.json file using jq
        json_data=$(jq --arg SCRIPT_NAME "$file_name" '.Name=$SCRIPT_NAME' automation/create_glue_job.json)
        json_data=$(jq --arg LOCATION "$s3_path/$file_name/main.py" '.Command.ScriptLocation=$LOCATION' <<< $json_data)

        # Create the glue job
        echo "Creating glue job $file_name"
        aws glue create-job --cli-input-json "$json_data"
      else
        # Set the script name in the glue_job.json file using jq
        json_data=$(jq --arg SCRIPT_NAME "$file_name" '.JobName=$SCRIPT_NAME' automation/update_glue_job.json)
        json_data=$(jq --arg LOCATION "$s3_path/$file_name/main.py" '.JobUpdate.Command.ScriptLocation=$LOCATION' <<< $json_data)

        # Update the glue job
        echo -e "\nUpdating glue job $file_name"
        aws glue update-job --cli-input-json "$json_data"
      fi

    else
      echo "main.py file does not exist in $dir_path."
    fi
done
