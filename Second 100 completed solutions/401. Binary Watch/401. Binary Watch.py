class Solution:
    def readBinaryWatch(self, turnedOn: int) -> List[str]:
        res = []

        for hr in range(12):
            for minute in range(60):
                leds_on = bin(hr).count("1") + bin(minute).count("1")

                if leds_on == turnedOn:
                    res.append(f"{hr}:{minute:02d}")

        return res