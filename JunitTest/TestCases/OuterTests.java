import org.junit.jupiter.api.Nested;
import org.junit.jupiter.api.Test;
import org.junit.jupiter.api.extension.ExtendWith;
import org.junit.jupiter.api.extension.ExtensionContext;
import org.junit.jupiter.api.extension.TestInstancePostProcessor;
import org.junit.jupiter.api.extension.TestInstancePreDestroyCallback;

@ExtendWith(OuterTests.LifecycleExtension.class)
class OuterTests {
    @Test
    void testOuter1() {
        System.out.println("testOuter1");
    }
    @Nested
    class InnerTests {
        @Test
        void testInner1() {
            System.out.println("testInner1");
        }
    }
    
    static class LifecycleExtension implements TestInstancePostProcessor, TestInstancePreDestroyCallback {
        //这个lifecycleExtension作为一个测试类内部的类
        @Override
        public void postProcessTestInstance(Object o, ExtensionContext extensionContext) throws Exception {
            System.out.println("postProcess: " + o);
        }
        @Override
        public void preDestroyTestInstance(ExtensionContext context) throws Exception{
            // preDestroy
            System.out.println("preDestroy: " + context.getRequiredTestInstance());
        }
    }
}
