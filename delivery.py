# Variables initialised on start-up
jetStreams = []
mileCost = 0

# Stores the dynamic programming results of the minimum cost of getting to the
# end point of that jetstream (matches jetstream index number as above)
endOfStreamCost = []

# Stores whether the matching jetstream (index) had it's minimal cost derived
# through a previous jetstream or none
prevStreamUsed = []


def findMinCostPath():
    '''Calculate the minimum cost of flying from the start to end'''
    '''for a swallow making efficient use of the jetstreams'''

    for i in range(0, len(jetStreams)):
        # Cost of walking to all the way to the current stream and then using it
        walkAllTheWay = getStretchCost(0, jetStreams[i][0]) + jetStreams[i][2]
        minCost = walkAllTheWay
        # Keep track that there was no previous stream we used here
        prevUsedStream = -1

        # Cost of using a previous stream and the current one
        for j in range(0, i):
            # Only use the stream if it's end is before the current's start
            if jetStreams[j][1] <= jetStreams[i][0]:
                curCost = usePreviousStreamCost(i, j)
            # All the streams from hereinafter,
            else:
                # have their end after the current's start so we stop
                break

            if curCost < minCost:
                minCost = curCost
                # Keep track of the chain of jetstreams we used
                prevUsedStream = j

        # Cost of using a previous stream but not the current one
        for j in range(0, i):
            curCost = endOfStreamCost[j] + \
                        getStretchCost(jetStreams[j][1], jetStreams[i][1])

            if curCost < minCost:
                minCost = curCost
                # Keep track of the chain of jetstreams we used
                prevUsedStream = j

        # Add the minimum cost to our memoisation storing minimum costs for JSes
        endOfStreamCost.append(minCost)
        prevStreamUsed.append(prevUsedStream)
    return endOfStreamCost[-1]


def usePreviousStreamCost(cur, prev):
    '''Calculate the cost of using a previous stream (given the index),'''
    '''walking to the current stream and then using the current stream'''

    #1) Best way to get to the previous stream has already been calculated.
    #2) The cost of walking from the previous jetstream to the current one.
    #3) The cost of using the current jetstream

    return endOfStreamCost[prev] + \
            getStretchCost(jetStreams[prev][1], jetStreams[cur][0]) + \
            jetStreams[cur][2]


def getStretchCost(start, end):
    '''Calculate the energy cost of travelling without a jetstream between'''
    '''a given start and end point'''

    return (end-start)*mileCost


def getOptimalJetStreams():
    '''Find the chain of jetstreams used for the optimal path based on the'''
    '''bread crumb trail we left behind'''

    i = len(prevStreamUsed) - 1         # We start at the last jetstream
    usingJetStreams = []

    # For each jetstream that used a previous jetstream
    while i != -1:
        # Extract just the start and end points
        usingJetStreams.append([jetStreams[i][0], jetStreams[i][1]])
        # and look at the next jetstream in the chain
        i = prevStreamUsed[i]

    # We remember to flip the list since we built it back-to-front
    usingJetStreams.reverse()
    return usingJetStreams



# MAIN/DRIVER
if __name__ == "__main__":
    try:
        with open('flight_paths.txt') as f:
            mileCost = int(f.readline())            # read first line
            for line in f:                          # read rest of lines
                jetStreams.append([int(x) for x in line.split()])
    except:
        print "Unexpected error while reading file"
        sys.exit(1)

    # Sort the jetstreams by their ending point
    jetStreams = sorted(jetStreams, key=lambda x:x[1])

    print findMinCostPath()
    print getOptimalJetStreams()
