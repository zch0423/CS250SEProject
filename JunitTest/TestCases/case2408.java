import java.util.stream.Stream;
import org.junit.jupiter.params.ParameterizedTest;
import org.junit.jupiter.params.provider.MethodSource;

public class case2408 {
    @ParameterizedTest
    @MethodSource("parameters")
    void test(Object object) {
    }

    private static Stream<Object> parameters() {
        return Stream.of(new Object() {
            @Override
            public String toString() {
                return null;
            }
// 传入了null
        });
    }
}

