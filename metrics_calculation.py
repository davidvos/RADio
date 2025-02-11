import datetime

import dart.Util
import dart.metrics.start_calculations


def main():
    # step 0: load config file
    config = dart.Util.read_full_config_file()

    articles, recommendations, behavior_file = dart.Util.read_files()

    print(str(datetime.datetime.now()) + "\tMetrics")
    dart.metrics.start_calculations.MetricsCalculator(config, articles, recommendations, behavior_file).execute()


if __name__ == "__main__":
    main()
