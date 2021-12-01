import java.io.File

fun List<String>.ints(): List<Int> = map{ it.toInt() }

open class Day(day: Int, year: Int, debug: Boolean = false) {
    init {
        println("AoC ${year}, day ${day}")
    }

    val inputFile = if (debug) { "sample.txt" } else { "input.txt"}

    val inputList : List<String> = File(inputFile).readLines()

    open fun title(): String = "Day x"

    open fun partOne(): Int {
        return 0
    }

    open fun partTwo(): Int {
        return 0
    }  

    init {
        println(partOne())
        println(partTwo())
    }
}


class Day1(debug: Boolean) : Day(1, 2021, debug) {
    override fun title()= "Sonar Sweep"

    override fun partOne() = solve(1)

    override fun partTwo() = solve(3)

    private fun solve(size: Int): Int {
        return inputList.ints()
            .windowed(size).map{ it.sum() }
            .windowed(2).count{ it.last() > it.first() }
    }
}

fun main(args: Array<String>) {
    Day1(args.size > 0)
}