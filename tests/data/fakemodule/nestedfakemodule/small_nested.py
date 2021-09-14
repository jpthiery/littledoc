# Copyright 2021 Jean-Pascal Thiery
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
# http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

"""
A small file documentation in nested module
"""


class ASmallSubClass:
    """
    A small sub class
    """

    def __init__(self, an_attribute):
        """
        Constructor of the small class
        :param an_attribute: a small attribute
        """
        self.an_attribute = an_attribute

    def a_function(self, a_parameter):
        """
        A small function of small class
        :param a_parameter: a small parameter
        :rtype: None
        """
        pass

    class ASmallNestedClasses:
        """
        A small nested class
        """

        def __init__(self):
            pass
