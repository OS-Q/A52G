"""
Arduino

Arduino Wiring-based Framework allows writing cross-platform software to
control devices attached to a wide range of Arduino boards to create all
kinds of creative coding, interactive objects, spaces or physical experiences.

http://arduino.cc/en/Reference/HomePage
"""

# Extends: https://github.com/platformio/platform-espressif32/blob/develop/builder/main.py

from os.path import abspath, isdir, isfile, join

from SCons.Script import DefaultEnvironment

env = DefaultEnvironment()
platform = env.PioPlatform()

FRAMEWORK_DIR = platform.get_package_dir("A52B")
assert isdir(FRAMEWORK_DIR)
BUILD_CORE = "esp32"

env.Append(
    ASFLAGS=["-x", "assembler-with-cpp"],

    CFLAGS=[
        "-std=gnu99",
        "-Wno-old-style-declaration"
    ],

    CCFLAGS=[
        "-Os",
        "-g3",
        "-Wall",
        "-nostdlib",
        "-Wpointer-arith",
        "-Wno-error=unused-but-set-variable",
        "-Wno-error=unused-variable",
        "-mlongcalls",
        "-ffunction-sections",
        "-fdata-sections",
        "-fstrict-volatile-bitfields",
        "-Wno-error=deprecated-declarations",
        "-Wno-error=unused-function",
        "-Wno-unused-parameter",
        "-Wno-sign-compare",
        "-fstack-protector",
        "-fexceptions",
        "-Werror=reorder"
    ],

    CXXFLAGS=[
        "-fno-rtti",
        "-fno-exceptions",
        "-std=gnu++11"
    ],

    LINKFLAGS=[
        "-nostdlib",
        "-Wl,-static",
        "-u", "call_user_start_cpu0",
        "-Wl,--undefined=uxTopUsedPriority",
        "-Wl,--gc-sections",
        "-Wl,-EL",
        "-T", "esp32.common.ld",
        "-T", "esp32.rom.ld",
        "-T", "esp32.peripherals.ld",
        "-T", "esp32.rom.libgcc.ld",
        "-T", "esp32.rom.spiram_incompatible_fns.ld",
        "-u", "ld_include_panic_highint_hdl",
        "-u", "__cxa_guard_dummy",
        "-u", "__cxx_fatal_exception"
    ],

    CPPDEFINES=[
        "ESP32",
        "ESP_PLATFORM",
        ("F_CPU", "$BOARD_F_CPU"),
        "HAVE_CONFIG_H",
        ("MBEDTLS_CONFIG_FILE", '\\"mbedtls/esp_config.h\\"'),
        ("ARDUINO", 10805),
        "ARDUINO_ARCH_ESP32",
        ("ARDUINO_VARIANT", '\\"%s\\"' % env.BoardConfig().get("build.variant").replace('"', "")),
        ("ARDUINO_BOARD", '\\"%s\\"' % env.BoardConfig().get("name").replace('"', ""))
    ],

    CPPPATH=[
        join(FRAMEWORK_DIR, "tools", "sdk", "include", "config"),
        join(FRAMEWORK_DIR, "tools", "sdk", "include", "app_trace"),
        join(FRAMEWORK_DIR, "tools", "sdk", "include", "app_update"),
        join(FRAMEWORK_DIR, "tools", "sdk", "include", "asio"),
        join(FRAMEWORK_DIR, "tools", "sdk", "include", "bootloader_support"),
        join(FRAMEWORK_DIR, "tools", "sdk", "include", "bt"),
        join(FRAMEWORK_DIR, "tools", "sdk", "include", "coap"),
        join(FRAMEWORK_DIR, "tools", "sdk", "include", "console"),
        join(FRAMEWORK_DIR, "tools", "sdk", "include", "driver"),
        join(FRAMEWORK_DIR, "tools", "sdk", "include", "esp-tls"),
        join(FRAMEWORK_DIR, "tools", "sdk", "include", "esp32"),
        join(FRAMEWORK_DIR, "tools", "sdk", "include", "esp_adc_cal"),
        join(FRAMEWORK_DIR, "tools", "sdk", "include", "esp_event"),
        join(FRAMEWORK_DIR, "tools", "sdk", "include", "esp_http_client"),
        join(FRAMEWORK_DIR, "tools", "sdk", "include", "esp_http_server"),
        join(FRAMEWORK_DIR, "tools", "sdk", "include", "esp_https_ota"),
        join(FRAMEWORK_DIR, "tools", "sdk", "include", "esp_ringbuf"),
        join(FRAMEWORK_DIR, "tools", "sdk", "include", "ethernet"),
        join(FRAMEWORK_DIR, "tools", "sdk", "include", "expat"),
        join(FRAMEWORK_DIR, "tools", "sdk", "include", "fatfs"),
        join(FRAMEWORK_DIR, "tools", "sdk", "include", "freemodbus"),
        join(FRAMEWORK_DIR, "tools", "sdk", "include", "freertos"),
        join(FRAMEWORK_DIR, "tools", "sdk", "include", "heap"),
        join(FRAMEWORK_DIR, "tools", "sdk", "include", "idf_test"),
        join(FRAMEWORK_DIR, "tools", "sdk", "include", "jsmn"),
        join(FRAMEWORK_DIR, "tools", "sdk", "include", "json"),
        join(FRAMEWORK_DIR, "tools", "sdk", "include", "libsodium"),
        join(FRAMEWORK_DIR, "tools", "sdk", "include", "log"),
        join(FRAMEWORK_DIR, "tools", "sdk", "include", "lwip"),
        join(FRAMEWORK_DIR, "tools", "sdk", "include", "mbedtls"),
        join(FRAMEWORK_DIR, "tools", "sdk", "include", "mdns"),
        join(FRAMEWORK_DIR, "tools", "sdk", "include", "micro-ecc"),
        join(FRAMEWORK_DIR, "tools", "sdk", "include", "mqtt"),
        join(FRAMEWORK_DIR, "tools", "sdk", "include", "newlib"),
        join(FRAMEWORK_DIR, "tools", "sdk", "include", "nghttp"),
        join(FRAMEWORK_DIR, "tools", "sdk", "include", "nvs_flash"),
        join(FRAMEWORK_DIR, "tools", "sdk", "include", "openssl"),
        join(FRAMEWORK_DIR, "tools", "sdk", "include", "protobuf-c"),
        join(FRAMEWORK_DIR, "tools", "sdk", "include", "protocomm"),
        join(FRAMEWORK_DIR, "tools", "sdk", "include", "pthread"),
        join(FRAMEWORK_DIR, "tools", "sdk", "include", "sdmmc"),
        join(FRAMEWORK_DIR, "tools", "sdk", "include", "smartconfig_ack"),
        join(FRAMEWORK_DIR, "tools", "sdk", "include", "soc"),
        join(FRAMEWORK_DIR, "tools", "sdk", "include", "spi_flash"),
        join(FRAMEWORK_DIR, "tools", "sdk", "include", "spiffs"),
        join(FRAMEWORK_DIR, "tools", "sdk", "include", "tcp_transport"),
        join(FRAMEWORK_DIR, "tools", "sdk", "include", "tcpip_adapter"),
        join(FRAMEWORK_DIR, "tools", "sdk", "include", "ulp"),
        join(FRAMEWORK_DIR, "tools", "sdk", "include", "vfs"),
        join(FRAMEWORK_DIR, "tools", "sdk", "include", "wear_levelling"),
        join(FRAMEWORK_DIR, "tools", "sdk", "include", "wifi_provisioning"),
        join(FRAMEWORK_DIR, "tools", "sdk", "include", "wpa_supplicant"),
        join(FRAMEWORK_DIR, "tools", "sdk", "include", "xtensa-debug-module"),
        join(FRAMEWORK_DIR, "tools", "sdk", "include", "esp-face"),
        join(FRAMEWORK_DIR, "tools", "sdk", "include", "esp32-camera"),
        join(FRAMEWORK_DIR, "tools", "sdk", "include", "esp-face"),
        join(FRAMEWORK_DIR, "tools", "sdk", "include", "fb_gfx"),
        join(FRAMEWORK_DIR, "cores", BUILD_CORE),
    ],

    LIBPATH=[
        join(FRAMEWORK_DIR, "tools", "sdk", "lib"),
        join(FRAMEWORK_DIR, "tools", "sdk", "ld")
    ],

    LIBS=[
        "-lgcc", "-lesp32", "-lphy", "-lesp_http_client", "-lmbedtls", "-lrtc", "-lesp_http_server", "-lbtdm_app", "-lspiffs", "-lbootloader_support", "-lmdns", "-lnvs_flash", "-lfatfs", "-lpp", "-lnet80211", "-ljsmn", "-lface_detection", "-llibsodium", "-lvfs", "-ldl_lib", "-llog", "-lfreertos", "-lcxx", "-lsmartconfig_ack", "-lxtensa-debug-module", "-lheap", "-ltcpip_adapter", "-lmqtt", "-lulp", "-lfd", "-lfb_gfx", "-lnghttp", "-lprotocomm", "-lsmartconfig", "-lm", "-lethernet", "-limage_util", "-lc_nano", "-lsoc", "-ltcp_transport", "-lc", "-lmicro-ecc", "-lface_recognition", "-ljson", "-lwpa_supplicant", "-lmesh", "-lesp_https_ota", "-lwpa2", "-lexpat", "-llwip", "-lwear_levelling", "-lapp_update", "-ldriver", "-lbt", "-lespnow", "-lcoap", "-lasio", "-lnewlib", "-lconsole", "-lapp_trace", "-lesp32-camera", "-lhal", "-lprotobuf-c", "-lsdmmc", "-lcore", "-lpthread", "-lcoexist", "-lfreemodbus", "-lspi_flash", "-lesp-tls", "-lwpa", "-lwifi_provisioning", "-lwps", "-lesp_adc_cal", "-lesp_event", "-lopenssl", "-lesp_ringbuf", "-lfr", "-lstdc++"
    ],

    LIBSOURCE_DIRS=[
        join(FRAMEWORK_DIR, "libraries")
    ],

    FLASH_EXTRA_IMAGES=[
        ("0x1000", join(FRAMEWORK_DIR, "tools", "sdk", "bin", "bootloader_${BOARD_FLASH_MODE}_${__get_board_f_flash(__env__)}.bin")),
        ("0x8000", join(env.subst("$BUILD_DIR"), "partitions.bin")),
        ("0xe000", join(FRAMEWORK_DIR, "tools", "partitions", "boot_app0.bin"))
    ]
)

if not env.BoardConfig().get("build.ldscript", ""):
    env.Replace(LDSCRIPT_PATH=env.BoardConfig().get("build.arduino.ldscript", ""))

#
# Target: Build Core Library
#

libs = []
if "build.variant" in env.BoardConfig():
    variants_dir = join(FRAMEWORK_DIR, "variants")
    if env.BoardConfig().get("build.variant") != "briki_mbcwb_esp32":
        # custom variant
        custom_variants_dir = "$PROJECT_DIR"
        env.Append(
            CPPDEFINES=["CUSTOM_VARIANT"],
            CPPPATH=[
                join(variants_dir,
                     "briki_mbcwb_esp32"),
                join(custom_variants_dir,
                     env.BoardConfig().get("build.variant"))
            ]
        )
        libs.append(env.BuildLibrary(
            join("$BUILD_DIR", "FrameworkArduinoVariant"),
            join(custom_variants_dir, env.BoardConfig().get("build.variant"))
        ))
    else:
        env.Append(
            CPPPATH=[
                join(variants_dir,
                    env.BoardConfig().get("build.variant"))
            ]
        )
        libs.append(env.BuildLibrary(
            join("$BUILD_DIR", "FrameworkArduinoVariant"),
            join(variants_dir, env.BoardConfig().get("build.variant"))
        ))

envsafe = env.Clone()

libs.append(envsafe.BuildLibrary(
    join("$BUILD_DIR", "FrameworkArduino"),
    join(FRAMEWORK_DIR, "cores", BUILD_CORE)
))

env.Prepend(LIBS=libs)

#
# Generate partition table
#

fwpartitions_dir = join(FRAMEWORK_DIR, "tools", "partitions")
partitions_csv = env.BoardConfig().get("build.partitions", "default.csv")
env.Replace(
    PARTITIONS_TABLE_CSV=abspath(
        join(fwpartitions_dir, partitions_csv) if isfile(
            join(fwpartitions_dir, partitions_csv)) else partitions_csv))

partition_table = env.Command(
    join("$BUILD_DIR", "partitions.bin"),
    "$PARTITIONS_TABLE_CSV",
    env.VerboseAction('"$PYTHONEXE" "%s" -q $SOURCE $TARGET' % join(
        FRAMEWORK_DIR, "tools", "gen_esp32part.py"),
                      "Generating partitions $TARGET"))
env.Depends("$BUILD_DIR/$PROGNAME$PROGSUFFIX", partition_table)