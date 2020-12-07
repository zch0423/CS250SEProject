import org.junit.jupiter.api.AfterAll;
import org.junit.jupiter.api.BeforeAll;
import org.junit.jupiter.api.DisplayName;
import org.junit.jupiter.api.Test;
import static org.junit.jupiter.api.Assertions.assertEquals;
@DisplayName("计算器程序")
class CalculatorTest {
    @BeforeAll
    public static void init(){
        System.out.println("开始测试");
    }
    @AfterAll
    public static void end(){
        System.out.println("结束测试");
    }
    @Test
    void add() {
        int result = Calculator.add(1, 2);
        assertEquals(3, result);
    }
}
//    @Test
//    void sub() {
//        int result = Calculator.sub(5, 3);
//        assertEquals(2, result);
//    }
//    @Test
//    void mul() {
//        int result = Calculator.mul(2, 5);
//        assertEquals(10, result);
//    }