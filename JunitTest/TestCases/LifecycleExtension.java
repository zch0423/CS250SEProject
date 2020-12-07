import org.junit.jupiter.api.extension.ExtensionContext;

public interface LifecycleExtension {
    void preDestroyTestInstance(ExtensionContext context);
}
