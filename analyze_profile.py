import pstats

stats = pstats.Stats('profile_results.txt')
stats.strip_dirs()
stats.sort_stats('cumulative')
stats.print_stats()
