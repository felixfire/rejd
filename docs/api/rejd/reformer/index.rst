  .. Copyright 2020 Konstruktor, Inc. All Rights Reserved.

  .. Licensed under the Apache License, Version 2.0 (the "License");
     you may not use this file except in compliance with the License.
     You may obtain a copy of the License at

  ..   http://www.apache.org/licenses/LICENSE-2.0

  .. Unless required by applicable law or agreed to in writing, software
     distributed under the License is distributed on an "AS IS" BASIS,
     WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
     See the License for the specific language governing permissions and
     limitations under the License.

 Copyright 2020 Vadim Sharay <vadimsharay@gmail.com>

 Licensed under the Apache License, Version 2.0 (the "License");
 you may not use this file except in compliance with the License.
 You may obtain a copy of the License at

     http://www.apache.org/licenses/LICENSE-2.0

 Unless required by applicable law or agreed to in writing, software
 distributed under the License is distributed on an "AS IS" BASIS,
 WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
 See the License for the specific language governing permissions and
 limitations under the License.

:mod:`rejd.reformer`
====================

.. py:module:: rejd.reformer


.. toctree::
   :titlesonly:
   :maxdepth: 3


Module Contents
---------------


.. data:: TYPES_MAP
   

   

.. function:: reform(schema: Dict, data: Any, initial_data: Any = None) -> Dict

   The main function that generates a new data structure according to the schema (JSONPath combination).

   .. code-block:: python

       # Usage example

       schema = {
           "source": "$",  # root data (initial_data)
           "type": "object",
           "properties": {  # fields schema for the new object
               "field1": {
                   "source": "@.field1 * 2",  # JSONPath
                   "type": "float"
               },
               "field2": {
                   "source": "@.array",
                   "type": "array",
                   "items": {
                       "source": "@.number"
                   }
               }
           }
       }

       data = {
           "field1": 1.5,
           "array": [
               {"number": 1},
               {"number": 2}
           ]
       }

       assert reform(schema, data) == {
           "field1": 3.0,
           "field2": [1, 2]
       }

   :param schema: You can create your own data structure according to the schema.
   :param data: Any input data
   :param initial_data: Initial data that will use as root (source: "$"). Default: data param value
   :return: new data with specific structure (according to the schema)
