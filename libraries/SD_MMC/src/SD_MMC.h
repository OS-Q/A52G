// Copyright 2015-2016 Espressif Systems (Shanghai) PTE LTD
//
// Licensed under the Apache License, Version 2.0 (the "License");
// you may not use this file except in compliance with the License.
// You may obtain a copy of the License at
//
//     http://www.apache.org/licenses/LICENSE-2.0
//
// Unless required by applicable law or agreed to in writing, software
// distributed under the License is distributed on an "AS IS" BASIS,
// WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
// See the License for the specific language governing permissions and
// limitations under the License.
#ifndef _SDMMC_H_
#define _SDMMC_H_

#if defined BRIKI_MBC_WB_SAMD
#error "Sorry, SD_MMC library doesn't work with samd21 processor"
#endif 

#include "FS.h"
#include "driver/sdmmc_types.h"
#include "sd_defines.h"

namespace fs
{

class SDMMCFS : public FS
{
protected:
    sdmmc_card_t* _card;

public:
    SDMMCFS(FSImplPtr impl);
    bool begin(const char * mountpoint="/sdcard", bool mode1bit=false);
    void end();
    sdcard_type_t cardType();
    uint64_t cardSize();
    uint64_t totalBytes();
    uint64_t usedBytes();
};

}

extern fs::SDMMCFS SD_MMC;

#endif /* _SDMMC_H_ */
