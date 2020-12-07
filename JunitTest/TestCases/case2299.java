
import org.junit.jupiter.api.BeforeEach;
        import org.junit.jupiter.api.Nested;
        import org.junit.jupiter.api.Test;

public class case2299 extends SuperClass {
    @Nested
    public class NestedClass extends SuperClass {
        @Test
        public void test() {
            // empty test
        }
    }
}

class SuperClass {
    @BeforeEach
    public void beforeEach() {
        System.out.println("beforeEach() for " + this.toString());
    }
}