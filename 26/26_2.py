

f = open("26_7014.txt").readlines()


n = int(f[0])
prices = [int(x) for x in f[1:]]

summary = []

def find_index(curr_prices, maxx):
    for x in range(len(curr_prices) - 1, -1, -1):
        if curr_prices[x] == maxx:
            return x


while prices:
    maxx = max(prices)
    maxx_index = find_index(prices, maxx)
    summary.append((maxx_index + 1) * maxx)
    prices = prices[maxx_index + 1:]

print(sum(summary), max(summary))