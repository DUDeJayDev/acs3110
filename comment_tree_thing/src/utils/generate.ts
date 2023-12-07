const names = [
    "Rob Banks",
    "Nick Everything",
    "Joe Tester",
    "Ben Dover",
    "Neil Down",
    "Anita Hero",
]

function getRandomCharacter() {
    // this syntax is hilarous
    // its actually faster than math.floor
    // please dont use it unless you know what it's doing.
    // https://jsperf.app/or-vs-floor/38
    return names[~~(names.length * Math.random())];
}

export { getRandomCharacter}
