# SPDX-FileCopyrightText: Copyright (c) 2022 NVIDIA CORPORATION & AFFILIATES. All rights reserved.
# SPDX-License-Identifier: Apache-2.0
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

from openroad_helpers import get_tables_OpenROAD_API
import argparse, os


if __name__ == "__main__":
  parser = argparse.ArgumentParser(description="Options to store the IR tables as .csv files, for a given design name and tech node.")
  parser.add_argument("-d", default="ac97_top", help="Give the design name. Default is ac97_top.")
  parser.add_argument("-t", default="ASAP7", help="Give the technology node. Default is ASAP7.")
  parser.add_argument("-def_file", default="ac97_top_fp.def.gz",  help="Give the def file to be read. Default is ac97_top_fp.def.gz .")
  parser.add_argument("-is_fp", default=False, action = 'store_true', help="Set this when the input def is of floorplan stage. Default is False.")
  parser.add_argument("-w", default=True, action = 'store_true', help="Set this when you want to write the dataframes as csv. Default is True.")
  parser.add_argument("-out_dir", default="NaN", help="Provide the output directory path to store IR tables. Default is IRs folder inside design directory.")
  args = parser.parse_args() 
   
  IRTables = get_tables_OpenROAD_API("../../", args.def_file, args.is_fp, args.w, True, args.d, args.t, args.out_dir)
  os._exit(0)
  
