# Copyright 2025 Google LLC
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#      http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

from google.cloud.modelarmor_v1 import Template


def get_model_armor_template(project_id: str, location: str, template_id: str) -> Template:
    # [START modelarmor_get_template]

    from google.api_core.client_options import ClientOptions
    from google.cloud.modelarmor_v1 import (
        ModelArmorClient,
        GetTemplateRequest,
    )

    client = ModelArmorClient(
        transport="rest",
        client_options=ClientOptions(api_endpoint=f"modelarmor.{location}.rep.googleapis.com"),
    )

    # TODO(Developer): Uncomment these variables and initialize
    # project_id = "YOUR_PROJECT_ID"
    # location = "us-central1"
    # template_id = "template_id"

    # Initialize request arguments
    request = GetTemplateRequest(
        name=f"projects/{project_id}/locations/{location}/templates/{template_id}",
    )

    # Make the request
    response = client.get_template(request=request)
    print(response.name)

# [END modelarmor_get_template]

    # Handle the response
    return response
