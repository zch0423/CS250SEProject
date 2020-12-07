import org.junit.jupiter.api.Test;
import org.junit.jupiter.api.TestInstance;
import org.junit.jupiter.api.extension.*;

@TestInstance(TestInstance.Lifecycle.PER_CLASS)
@ExtendWith({ Dummy2Test.Extension1.class, Dummy2Test.Extension2.class })
public class Dummy2Test {
//    private static final Logger LOG = Logger.getLogger(Dummy2Test.class.getName());

    @Test
    public void justATest() {
//        LOG.fine("@Test");
        System.out.println("@Test");
    }

    public static class Extension1 implements BeforeAllCallback, AfterAllCallback, TestInstancePostProcessor, TestInstancePreDestroyCallback {

        @Override
        public void beforeAll(ExtensionContext ec) throws Exception {
//            LOG.warning("Extension1.beforeAll");
            System.out.println("Extension1.beforeAll");
        }

        @Override
        public void afterAll(ExtensionContext ec) throws Exception {
//            LOG.warning("Extension1.afterAll");
            System.out.println("Extension1.afterAll");
        }

        @Override
        public void postProcessTestInstance(Object o, ExtensionContext ec) throws Exception {
//            LOG.warning("Extension1.postProcessTestInstance");
            System.out.println("Extension1.postProcessTestInstance");
        }

        @Override
        public void preDestroyTestInstance(ExtensionContext ec) throws Exception {
//            LOG.warning("Extension1.preDestroyTestInstance");
            System.out.println("Extension1.preDestroyTestInstance");
        }

    }

    public static class Extension2 implements BeforeAllCallback, AfterAllCallback , TestInstancePostProcessor, TestInstancePreDestroyCallback {

        @Override
        public void beforeAll(ExtensionContext ec) throws Exception {
//            LOG.warning("Extension2.beforeAll");
            System.out.println("Extension2.beforeAll");
        }

        @Override
        public void afterAll(ExtensionContext ec) throws Exception {
//            LOG.warning("Extension2.afterAll");
            System.out.println("Extension2.afterAll");
        }

        @Override
        public void postProcessTestInstance(Object o, ExtensionContext ec) throws Exception {
//            LOG.warning("Extension2.postProcessTestInstance");
            System.out.println("Extension2.postProcessTestInstance");
        }

        @Override
        public void preDestroyTestInstance(ExtensionContext ec) throws Exception {
//            LOG.warning("Extension2.preDestroyTestInstance");
            System.out.println("Extension2.preDestroyTestInstance");
        }
    }
}