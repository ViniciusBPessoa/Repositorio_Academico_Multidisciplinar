/**
 * Access token payload.
 */
export interface AccessToken {
  /**
   * Version number. Old tokens will be invalid.
   */
  version: number;

  /**
   * User id for new Version or User Uuid for old versions.
   */
  id: string;
}
