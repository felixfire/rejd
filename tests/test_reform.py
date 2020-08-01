# Copyright 2020 Vadim Sharay <vadimsharay@gmail.com>
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

import pytest

from rejd.reformer import reform


class TestReform:
    def test_simple_dict(self):
        assert reform(
            {
                "source": "$",
                "type": "object",
                "properties": {"prop1": {"source": "@.id"}},
            },
            {"id": 1},
        ) == {"prop1": 1}

    def test_simple_list(self):
        assert reform(
            {"source": "$", "type": "array", "items": {"source": "@.id"}}, [{"id": 1}]
        ) == [1]

    def test_nested_dict(self):
        assert reform(
            {
                "source": "$",
                "type": "object",
                "properties": {"prop1": {"source": "@.np.id"}},
            },
            {"np": {"id": 1}},
        ) == {"prop1": 1}

    def test_nested_list(self):
        assert reform(
            {"source": "$", "type": "array", "items": {"source": "@[:].id"}},
            [{"id": 1}, {"id": 2}],
        ) == [1, 2]

    def test_nested(self):
        assert reform(
            {
                "source": "$",
                "type": "array",
                "items": {
                    "source": "@",
                    "type": "object",
                    "properties": {"prop": {"source": "@.id"}},
                },
            },
            [{"id": 1}, {"id": 2}],
        ) == [{"prop": 1}, {"prop": 2}]

    def test_no_source(self):
        assert reform(
            {"type": "array", "items": {"type": "object"}}, [{"id": 1}, {"id": 2}]
        ) == [{"id": 1}, {"id": 2}]

    def test_no_source_with_default(self):
        assert reform(
            {"type": "array", "items": {"type": "int", "default": "1"}},
            [{"id": 1}, {"id": 2}],
        ) == [1, 1]

    def test_no_type(self):
        assert reform({"source": "@[0].id"}, [{"id": 1}, {"id": 2}]) == 1

    def test_bad_props_schema(self):
        with pytest.raises(ValueError):
            reform(
                {"source": "$", "type": "object", "properties": []},
                [{"id": 1}, {"id": 2}],
            )

    def test_bad_items_schema(self):
        with pytest.raises(ValueError):
            reform(
                {"source": "$", "type": "array", "items": []}, [{"id": 1}, {"id": 2}]
            )
