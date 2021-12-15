import io.github.rybalkinsd.kohttp.dsl.httpGet
import io.github.rybalkinsd.kohttp.ext.asString
import io.github.rybalkinsd.kohttp.ext.url

fun main() {

    val searchs = arrayOf("李 白","李白","李%20白","W+")
    val url = "http://zhuaowei.top:8081/poetry/content"
    searchs.forEach { s->
        val result = httpGet {
            url(url)
            param {
                "content" to s
            }
        }.asString()
        println("""【${s}】的搜索结果为：""")
        println(result)
        println()
    }


}